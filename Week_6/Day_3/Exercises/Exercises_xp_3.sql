-- Exercise 1: DVD Rental

-- List all languages:
SELECT * FROM language;

-- List films with their languages:
SELECT f.title, f.description, l.name AS language_name
FROM film f
INNER JOIN language l ON f.language_id = l.language_id;

-- All languages:
SELECT f.title, f.description, l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;

-- Create new_film:
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES ('Interstellar'), ('Oppenheimer');

-- Create customer_review with the ON DELETE CASCADE constraint:
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add 2 reviews (linking to the IDs created in new_film):
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Masterpiece', 10, 'A visual and emotional journey through space.'),
(2, 1, 'Powerful', 9, 'Incredible acting and sound design.');



