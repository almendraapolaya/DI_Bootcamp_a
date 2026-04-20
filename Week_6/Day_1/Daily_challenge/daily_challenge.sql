-- 1. Create the table
CREATE TABLE actors (
    actors_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

-- 2. Inserting the data 
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('George', 'Clooney', '1961-05-06', 2),
('Meryl', 'Streep', '1949-06-22', 3),
('Michelle', 'Yeoh', '1962-08-6', 1),
('Matt', 'Damon', '1970-10-08', 5),
('Meryl', 'Streep', '1949-06-22',3);

-- 1. Count how many actors are in the table.

SELECT COUNT(*) FROM actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?:

--INSERT INTO actors (first_name, last_name, age, number_oscars) 
--VALUES ('Brad', NULL, '1963-12-18', 2);