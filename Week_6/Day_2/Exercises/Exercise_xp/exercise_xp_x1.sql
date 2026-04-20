-- Day1

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price INT NOT NULL
);

-- customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

INSERT INTO items (item_name, price) VALUES 
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name) VALUES 
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM customers;
SELECT * FROM items;

-- 1. Fetch all the items: 
SELECT * FROM items;

-- 2. Items with a price above 80 (80 not included):
SELECT * FROM items 
WHERE price > 80;

-- 3. Items with a price below 300 (300 included)
SELECT * FROM items 
WHERE price <= 300;

-- 4. Customers whose last name is ‘Smith’
SELECT * FROM customers 
WHERE last_name = 'Smith';

-- 5. Customers whose last name is ‘Jones’:
SELECT * FROM customers 
WHERE last_name = 'Jones';

-- 6. Customers whose first name is NOT ‘Scott’:
SELECT * FROM customers 
WHERE first_name != 'Scott';

-- Day_2 - Exercise_XP:
-- Exercise 1 : Items and customers

-- 1. All items, ordered by price (lowest to highest)
SELECT * FROM items ORDER BY price ASC;

-- 2. Items with a price >= 80, ordered highest to lowest
SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

-- 3. First 3 customers by first name (A-Z) - excluding the ID
SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3;

-- 4. All last names in reverse alphabetical order (Z-A)
SELECT last_name FROM customers ORDER BY last_name DESC;

