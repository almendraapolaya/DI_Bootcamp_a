-- Exercises XP

SET search_path TO movies, public;

SELECT count(*) FROM movies.country;

SELECT count(*) FROM movies.movie_genres;

SELECT count(*) FROM movies.movie_company;

-- EXERCISE 1: Movie Rankings and Analysis:

-- Task 1: Rank Movies by Popularity within Each Genre:

SET search_path TO movies, public;

SELECT 
    g.genre_name, 
    m.title, 
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) as popularity_rank
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, popularity_rank;

-- Task 2: dentify the Top 3 Movies by Revenue within Each Production Company
SET search_path TO movies, public;

SELECT 
    pc.company_name, 
    m.title, 
    m.revenue,
    NTILE(4) OVER (PARTITION BY pc.company_id ORDER BY m.revenue DESC) as revenue_quartile
FROM movie m
JOIN movie_company mc ON m.movie_id = mc.movie_id
JOIN production_company pc ON mc.company_id = pc.company_id
WHERE m.revenue > 0
ORDER BY pc.company_name, m.revenue DESC;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre:

SET search_path TO movies, public;

SELECT 
    g.genre_name, 
    m.title, 
    m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_id 
        ORDER BY m.release_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_total_budget
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, m.release_date;

-- Task 4: Identify the Most Recent Movie for Each Genre:

SET search_path TO movies, public;

SELECT DISTINCT
    g.genre_name,
    FIRST_VALUE(m.title) OVER (
        PARTITION BY g.genre_id 
        ORDER BY m.release_date DESC
    ) as most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (
        PARTITION BY g.genre_id 
        ORDER BY m.release_date DESC
    ) as release_date
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name;

-- EXERCISE 2: Cast and Crew Performance Analysis:

-- Task1:Rank Actors by Their Appearance in Movies:

SET search_path TO movies, public;

SELECT 
    p.person_name, 
    COUNT(mc.movie_id) AS movie_count,
    DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) as appearance_rank
FROM person p
JOIN movie_cast mc ON p.person_id = mc.person_id
GROUP BY p.person_id, p.person_name
ORDER BY appearance_rank;

-- Task2: Identify the Top Director by Average Movie Rating:

SET search_path TO movies, public;

WITH director_ratings AS (
    SELECT 
        p.person_name,
        AVG(m.vote_average) as avg_rating
    FROM person p
    JOIN movie_crew mc ON p.person_id = mc.person_id
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE mc.job = 'Director'
    GROUP BY p.person_id, p.person_name
)
SELECT 
    person_name, 
    ROUND(avg_rating, 2) as average_rating,
    RANK() OVER (ORDER BY avg_rating DESC) as rating_rank
FROM director_ratings
ORDER BY rating_rank
LIMIT 10;

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor:

SET search_path TO movies, public;

SELECT DISTINCT
    p.person_name,
    SUM(m.revenue) OVER (PARTITION BY p.person_id) as cumulative_revenue
FROM person p
JOIN movie_cast mc ON p.person_id = mc.person_id
JOIN movie m ON mc.movie_id = m.movie_id
ORDER BY cumulative_revenue DESC;

-- Task4: Identify the Director Whose Movies Have the Highest Total Budget

SET search_path TO movies, public;

WITH director_budgets AS (
    SELECT 
        p.person_name,
        SUM(m.budget) as total_budget
    FROM person p
    JOIN movie_crew mc ON p.person_id = mc.person_id
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE mc.job = 'Director'
    GROUP BY p.person_id, p.person_name
)
SELECT 
    person_name, 
    total_budget
FROM (
    SELECT 
        person_name, 
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) as budget_rank
    FROM director_budgets
) ranked_budgets
WHERE budget_rank = 1;