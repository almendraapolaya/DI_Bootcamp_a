-- Daily Challenge:

--EXERCISE 1: Detailed Medal Analysis:

-- Task 1: 

-- Create temp table for dual-season medalists:
CREATE TEMP TABLE dual_season_medalists AS
WITH medal_counts AS (
    SELECT 
        p.id AS person_id,
        p.full_name,
        g.season,
        COUNT(ce.medal_id) AS medal_count
    FROM olympics.person p
    JOIN olympics.games_competitor gc ON p.id = gc.person_id
    JOIN olympics.games g ON gc.games_id = g.id
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.medal m ON ce.medal_id = m.id
    WHERE m.medal_name <> 'NA'
    GROUP BY p.id, p.full_name, g.season
)
SELECT 
    s.full_name,
    s.medal_count AS summer_medals,
    w.medal_count AS winter_medals
FROM medal_counts s
JOIN medal_counts w ON s.person_id = w.person_id
WHERE s.season = 'Summer' AND w.season = 'Winter';

-- Display the result: 
SELECT * FROM dual_season_medalists;

-- Task 2:

-- Create temp table for multi-sport medalists:
CREATE TEMP TABLE two_sport_medalists AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(ce.medal_id) AS total_medals
FROM olympics.person p
JOIN olympics.games_competitor gc ON p.id = gc.person_id
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.medal m ON ce.medal_id = m.id
WHERE m.medal_name <> 'NA'
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT e.sport_id) = 2;

-- Display the top 3 with highest total medals:
SELECT * FROM two_sport_medalists
ORDER BY total_medals DESC
LIMIT 3;

-- EXERCISE 2: Region and Competitor Performance:

-- Task 1: 

--Region and Competitor Performance
SELECT 
    r.region_name, 
    SUM(max_medals_in_event) AS total_regional_medals
FROM olympics.noc_region r
JOIN olympics.person_region pr ON r.id = pr.region_id
JOIN (
    -- Highest number of medals in one event per competitor:
    SELECT 
        gc.person_id, 
        MAX(event_medal_count) as max_medals_in_event
    FROM (
        SELECT competitor_id, event_id, COUNT(medal_id) as event_medal_count
        FROM olympics.competitor_event
        WHERE medal_id <> 4 
        GROUP BY competitor_id, event_id
    ) sub_event
    JOIN olympics.games_competitor gc ON sub_event.competitor_id = gc.id
    GROUP BY gc.person_id
) person_max ON pr.person_id = person_max.person_id
GROUP BY r.region_name
ORDER BY total_regional_medals DESC
LIMIT 5;

-- Task 2:

-- Create temp table for persistent participants:
CREATE TEMP TABLE persistent_non_medalists AS
SELECT 
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_count
FROM olympics.person p
JOIN olympics.games_competitor gc ON p.id = gc.person_id
-- Left join with medals to filter them out:
LEFT JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
LEFT JOIN olympics.medal m ON ce.medal_id = m.id AND m.medal_name <> 'NA'
GROUP BY p.id, p.full_name
-- Participated in more than 3 games AND has zero actual medals:
HAVING COUNT(DISTINCT gc.games_id) > 3 
   AND COUNT(m.id) = 0;

-- Display the contents:
SELECT * FROM persistent_non_medalists
ORDER BY games_count DESC;
