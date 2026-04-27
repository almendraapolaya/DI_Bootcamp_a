--
-- Daily Challenge: Advanced Movie Data Analysis
--
-- Task 1: Calculate the Avergae Budget Growth Rate for Each Production

SET search_path TO movies, public;

WITH budget_diffs AS (
    SELECT 
        pc.company_name,
        m.title,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date) as prev_budget
    FROM movie m
    JOIN movie_company mc ON m.movie_id = mc.movie_id
    JOIN production_company pc ON mc.company_id = pc.company_id
    WHERE m.budget > 0
),
growth_rates AS (
    SELECT 
        company_name,
        -- Growth rate formula: 
        CASE 
            WHEN prev_budget IS NOT NULL AND prev_budget > 0 
            THEN (budget - prev_budget)::float / prev_budget 
            ELSE NULL 
        END as growth_rate
    FROM budget_diffs
)
SELECT 
    company_name, 
    ROUND(AVG(growth_rate)::numeric, 4) as avg_growth_rate
FROM growth_rates
WHERE growth_rate IS NOT NULL
GROUP BY company_name
ORDER BY avg_growth_rate DESC;

-- Task 2: Determine the Most Consistently High-Rated Actor

SET search_path TO movies, public;

WITH global_avg AS (
    SELECT AVG(vote_average) as overall_avg FROM movie
),
high_rated_appearances AS (
    SELECT 
        p.person_name,
        COUNT(*) as high_rated_movie_count
    FROM person p
    JOIN movie_cast mc ON p.person_id = mc.person_id
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE m.vote_average > (SELECT overall_avg FROM global_avg)
    GROUP BY p.person_id, p.person_name
)
SELECT 
    person_name, 
    high_rated_movie_count,
    RANK() OVER (ORDER BY high_rated_movie_count DESC) as consistency_rank
FROM high_rated_appearances
ORDER BY high_rated_movie_count DESC
LIMIT 1;

-- Task 3: Calculate the Rolling Average Revenue for Each Genre

SET search_path TO movies, public;

SELECT 
    g.genre_name, 
    m.title, 
    m.release_date,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_id 
        ORDER BY m.release_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as rolling_avg_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, m.release_date;

-- Task 4: Identify the Highest-Grossing Movie Series

SET search_path TO movies, public;

WITH keyword_revenue AS (
    SELECT 
        k.keyword_name,
        m.title,
        m.revenue
    FROM movie m
    JOIN movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN keyword k ON mk.keyword_id = k.keyword_id
)
SELECT 
    keyword_name as series_keyword,
    SUM(revenue) as total_series_revenue,
    COUNT(title) as movie_count
FROM keyword_revenue
GROUP BY keyword_name
HAVING COUNT(title) > 1  
ORDER BY total_series_revenue DESC
LIMIT 1;