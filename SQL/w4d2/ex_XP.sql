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
--------------------------
-- EX XP GOLD
--------------------------
-- 1)
SELECT rating,
    COUNT(*) AS film_count
FROM film
GROUP BY rating;
--------------------------
SELECT film_id,
    title,
    rating,
    length,
    rental_rate
FROM film
WHERE rating IN ('G', 'PG-13')
    AND length < 120
    AND rental_rate < 3.00
ORDER BY title;
--------------------------
UPDATE customer
SET first_name = 'MyFirstName',
    last_name = 'MyLastName'
WHERE customer_id = 1;
--------------------------
UPDATE customer
SET address = 'MyAddress'
WHERE customer_id = 1;
--------------------------
-- 2)
-- UPDATE
UPDATE students
SET birth_date = '02-11-1998'
WHERE last_name = 'Benichou';
--------------------------
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David';
--------------------------
--DELETE
DELETE FROM students
WHERE first_name = 'Lea'
    AND last_name = 'Benichou';
--------------------------
--COUNT
SELECT COUNT(*) AS total_students
FROM students;
--------------------------
SELECT COUNT(*) AS students_born_after_2000
FROM students
WHERE birth_date > '2000-01-01';
--------------------------
--INSERT/ALTER
ALTER TABLE students
ADD COLUMN math_grade int DEFAULT 0;
--------------------------
UPDATE students
SET math_grade = math_grade + 80
WHERE id = 1;
--------------------------
UPDATE students
SET math_grade = math_grade + 90
WHERE id = 2
    or id = 4;
--------------------------
UPDATE students
SET math_grade = math_grade + 40
WHERE id = 6;
--------------------------
SELECT COUNT(*) AS students_with_grade_above_83
FROM students
WHERE math_grade > 83;
--------------------------
INSERT INTO students (first_name, last_name, birth_date, math_grade)
values (
        'Omer',
        'Simpson',
        (
            SELECT birth_date
            FROM students
            WHERE first_name = 'Omer'
                AND last_name = 'Simpson'
        ),
        70
    );
--------------------------
SELECT first_name,
    last_name,
    COUNT(math_grade) AS total_grades
FROM students
GROUP BY first_name,
    last_name;
--------------------------
SELECT SUM(math_grade) AS total_grades_sum
FROM students;
--------------------------
-- 3)
CREATE TABLE purchases (
    id integer primary key generated always as identity,
    customer_id int REFERENCES customers(id),
    item_id int REFERENCES items(id),
    quantity_purchased int
);
--------------------------
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
        (
            SELECT id
            FROM customers
            WHERE first_name = 'Scott'
                AND last_name = 'Scott'
        ),
        (
            SELECT id
            FROM items
            WHERE item = 'Fan'
        ),
        1
    ),
    (
        (
            SELECT id
            FROM customers
            WHERE first_name = 'Melanie'
                AND last_name = 'Johnson'
        ),
        (
            SELECT id
            FROM items
            WHERE item = 'Large Desk'
        ),
        10
    ),
    (
        (
            SELECT id
            FROM customers
            WHERE first_name = 'Greg'
                AND last_name = 'Jones'
        ),
        (
            SELECT id
            FROM items
            WHERE item = 'Small Desk'
        ),
        2
    );
--------------------------
SELECT *
FROM purchases;
-- All purchases. Is this information useful to us? Hell nah, just a bunch of numbers / id's that mean nothing to a human
--------------------------
SELECT p.*,
    c.first_name,
    c.last_name
FROM purchases p
    JOIN customers c ON p.customer_id = c.id;
--------------------------
SELECT *
FROM purchases
WHERE customer_id = 5;
-- OR
SELECT p.*,
    c.first_name,
    c.last_name
FROM purchases p
    JOIN customers c ON p.customer_id = c.id
WHERE c.id = 5;
--------------------------
SELECT *
FROM purchases p
    JOIN items i ON p.item_id = i.id
WHERE i.item IN ('Large Desk', 'Small Desk');
--------------------------
SELECT c.first_name,
    c.last_name,
    i.item
FROM purchases p
    JOIN customers c ON c.id = p.customer_id
    JOIN items i ON i.id = p.item_id;
--------------------------
-- adding a row with a blank item reference will work if the "item_id" column allows NULL values or is not defined as a foreign key. 
-- However, if it is defined as a foreign key with a NOT NULL constraint, the database will not allow inserting a row without a valid item reference.