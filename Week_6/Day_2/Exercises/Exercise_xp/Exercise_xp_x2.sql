-- Exercise 2 : dvdrental database

-- 1. Select all columns from customer:
SELECT * FROM customer;

-- 2. Names with an alias "full_name":
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- 3. Unique account creation dates:
SELECT DISTINCT create_date FROM customer;

-- 4. Customer details, descending order by first name:
SELECT * FROM customer 
ORDER BY first_name DESC;

-- 5. Film details, ascending order by rental rate:
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

-- 6. Customers in Texas (from the address table):
SELECT address, phone 
FROM address 
WHERE district = 'Texas';

-- 7. Movie IDs 15 or 150:
SELECT * FROM film 
WHERE film_id = 15 OR film_id = 150;

-- 8. Check for a favorite movie:
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'MAMMA MIA';

-- 9. Search by first two letters:
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'MA%';

-- 10. The 10 cheapest movies:
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;

-- 11. The NEXT 10 cheapest movies:
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10 OFFSET 10;

-- 12. Join customer and payment:
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Movies NOT in inventory:
SELECT f.title
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

-- 14. Cities and their Countries:
SELECT city.city, country.country
FROM city
JOIN country ON city.country_id = country.country_id;

-- 15. Bonus: Payments ordered by staff ID
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;
