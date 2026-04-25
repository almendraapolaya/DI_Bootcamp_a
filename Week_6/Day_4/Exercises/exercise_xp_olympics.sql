-- Exercise 1:
--Task 1:
SELECT 
    m.medal_name, 
    (SELECT ROUND(AVG(gc.age), 2)
     FROM olympics.games_competitor gc
     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
     WHERE ce.medal_id = m.id 
       AND gc.age > 0 
    ) AS average_age
FROM olympics.medal m
WHERE m.medal_name <> 'NA' 
ORDER BY average_age DESC;

-- Task 2:

SELECT 
    r.region_name, 
    COUNT(DISTINCT pr.person_id) AS versatile_athlete_count
FROM olympics.noc_region r
JOIN olympics.person_region pr ON r.id = pr.region_id
WHERE pr.person_id IN (
    -- Find athletes with more than 3 unique events:
    SELECT gc.person_id
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY r.region_name
ORDER BY versatile_athlete_count DESC
LIMIT 5;

-- Task 3:
CREATE TEMP TABLE medal_leaders AS
SELECT person_id, total_medals
FROM (
    SELECT gc.person_id, COUNT(ce.medal_id) AS total_medals
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.medal m ON ce.medal_id = m.id
    WHERE m.medal_name <> 'NA' 
    GROUP BY gc.person_id
) AS subquery
WHERE total_medals > 2;

-- Temporary table:
SELECT * FROM medal_leaders ORDER BY total_medals DESC;

-- Task 4:
-- Step 1: Create the audit table:
CREATE TEMP TABLE competitor_audit AS 
SELECT id, full_name FROM olympics.person;

-- Step 2: Delete those who have NO medals:
DELETE FROM competitor_audit
WHERE id NOT IN (
    SELECT DISTINCT gc.person_id
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.medal m ON ce.medal_id = m.id
    WHERE m.medal_name <> 'NA'
);

-- Step 3: See how many people are left:
SELECT COUNT(*) FROM competitor_audit;



-- Exercise 2:


UPDATE olympics.person p
SET height = (
    SELECT ROUND(AVG(p2.height), 2)
    FROM olympics.person p2
    JOIN olympics.person_region pr2 ON p2.id = pr2.person_id
    JOIN olympics.person_region pr1 ON p.id = pr1.person_id
    WHERE pr2.region_id = pr1.region_id
      AND p2.height > 0 
)
WHERE p.height = 0;

-- Task 2:

CREATE TEMP TABLE single_games_multi_events AS
SELECT person_id, games_id, event_count
FROM (
    SELECT gc.person_id, gc.games_id, COUNT(ce.event_id) AS event_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id, gc.games_id
    HAVING COUNT(ce.event_id) > 1
) AS subquery;

-- Busiest athletes at the top:
SELECT * FROM single_games_multi_events ORDER BY event_count DESC LIMIT 10;

-- Task 3:

SELECT r.region_name
FROM olympics.noc_region r
JOIN olympics.person_region pr ON r.id = pr.region_id
JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
JOIN olympics.medal m ON ce.medal_id = m.id
WHERE m.medal_name <> 'NA'
GROUP BY r.region_name
HAVING COUNT(ce.medal_id)::FLOAT / COUNT(DISTINCT pr.person_id) > (
    --Global average medals per athlete:
    SELECT COUNT(ce2.medal_id)::FLOAT / COUNT(DISTINCT gc2.person_id)
    FROM olympics.games_competitor gc2
    JOIN olympics.competitor_event ce2 ON gc2.id = ce2.competitor_id
    JOIN olympics.medal m2 ON ce2.medal_id = m2.id
    WHERE m2.medal_name <> 'NA'
);

-- Task 4:

CREATE TEMP TABLE dual_season_athletes AS
SELECT p.id, p.full_name
FROM olympics.person p
WHERE p.id IN (
    SELECT gc.person_id FROM olympics.games_competitor gc 
    JOIN olympics.games g ON gc.games_id = g.id WHERE g.season = 'Summer'
)
AND p.id IN (
    SELECT gc.person_id FROM olympics.games_competitor gc 
    JOIN olympics.games g ON gc.games_id = g.id WHERE g.season = 'Winter'
);

-- Checking how many athletes actually did both:
SELECT * FROM dual_season_athletes;