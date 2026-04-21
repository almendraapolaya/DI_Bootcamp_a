--Daily Challenge: SQL Puzzle:

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab (id, name) VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab (id) VALUES
(5),
(NULL);

-- VERIFICATION:
SELECT * FROM FirstTab;
SELECT * FROM SecondTab;

-- QUESTIONS: 

-- Q1: What will be the OUTPUT of the following statement? 
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
--Result = 0

-- Q2: What will be the OUTPUT of the following statement? 
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- Result = 2

-- Q3: What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- Result = 0

-- Q4: What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- Result = 2