-- EX XP 
-- 1)
--------------------------
SELECT *
FROM items
ORDER BY price;
--------------------------
SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;
--------------------------
SELECT first_name,
    last_name
FROM customers
WHERE id <= 3
ORDER BY first_name;
--------------------------
SELECT last_name
FROM customers
ORDER BY last_name DESC;
--------------------------
--------------------------
-- 2)
--------------------------
--1
SELECT *
from customer;
--------------------------
--2
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customer;
--------------------------
--3
SELECT DISTINCT create_date
FROM customer;
-- Im not quite sure that's what you wanted me to do as all the create_date are the same (2006-02-14) so it will only return one thing
--------------------------
--4
SELECT *
FROM customer
ORDER BY first_name DESC;
--------------------------
--5
SELECT film_id,
    title,
    description,
    release_year,
    rental_rate
FROM film
ORDER BY rental_rate;
--------------------------
--6
SELECT address,
    phone
FROM address
WHERE district = 'Texas';
--------------------------
--7
SELECT *
FROM film
WHERE film_id = 15
    or film_id = 150;
--------------------------
--8
SELECT film_id,
    title,
    description,
    length,
    rental_rate
FROM film
WHERE title = 'Splash Gump';
--------------------------
--9
SELECT film_id,
    title,
    description,
    length,
    rental_rate
FROM film
WHERE title like 'Sp%';
--------------------------
--10
SELECT *
from film
ORDER BY rental_rate
LIMIT 10;
--------------------------
--11
SELECT *
from film
ORDER BY rental_rate OFFSET 10 FETCH NEXT 10 ROWS ONLY;
--------------------------
--12
SELECT customer.first_name,
    customer.last_name,
    payment.amount,
    payment.payment_date
FROM customer
    JOIN payment ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id,
    payment.payment_id;
--------------------------
--13
SELECT film.film_id,
    title,
    description,
    length,
    rental_rate
FROM film
    LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL;
--------------------------
--14
SELECT city.city AS City,
    country.country AS Country
FROM city
    JOIN country ON city.country_id = country.country_id;
--------------------------
--15
SELECT customer.customer_id,
    customer.first_name,
    customer.last_name,
    payment.amount,
    payment.payment_date
FROM customer
    JOIN payment ON customer.customer_id = payment.customer_id
    JOIN staff ON payment.staff_id = staff.staff_id
ORDER BY staff.staff_id;