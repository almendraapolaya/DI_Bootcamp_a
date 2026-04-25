-- Exercise 2 : DVD Rental

-- Count of outstanding rentals:
SELECT count(*) FROM rental WHERE return_date IS NULL;

-- 30 most expensive outstanding movies (based on replacement cost):
SELECT f.title, f.replacement_cost
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

-- The 1st film (Sumo):
SELECT f.title FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo wrestler%'
AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- The 3rd film (Matthew's July return):
SELECT f.title FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01'
AND f.rental_rate > 4.00;