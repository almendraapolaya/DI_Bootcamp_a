-- Daily Challenge: Tables Relationships
-- Part 1:

-- Create the Customer table:
CREATE TABLE app_customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE app_customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE REFERENCES app_customer(id) ON DELETE CASCADE
);

-- Insert Customers:
INSERT INTO app_customer (first_name, last_name) VALUES 
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert Profiles using Subqueries:
-- John is loggedIn
INSERT INTO app_customer_profile (isLoggedIn, customer_id)
VALUES (true, (SELECT id FROM app_customer WHERE first_name = 'John'));

-- Jerome is NOT logged in (false)
INSERT INTO app_customer_profile (isLoggedIn, customer_id)
VALUES (false, (SELECT id FROM app_customer WHERE first_name = 'Jerome'));

--The first_name of the LoggedIn customers:
SELECT c.first_name 
FROM app_customer c
INNER JOIN app_customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

--All customers first_name and isLoggedIn columns:
SELECT c.first_name, cp.isLoggedIn
FROM app_customer c
LEFT JOIN app_customer_profile cp ON c.id = cp.customer_id;

--The number of customers that are not LoggedIn:
SELECT COUNT(*) 
FROM app_customer c
LEFT JOIN app_customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn IS NOT TRUE;