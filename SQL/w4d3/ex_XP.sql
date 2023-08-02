-- EX XP
--------------------------
-- 1)
--1
SELECT name AS all_film_languages
FROM language;
--------------------------
--2
SELECT film.title,
    film.description,
    language.name AS language_name
FROM film
    LEFT JOIN language ON film.language_id = language.language_id --------------------------
SELECT film.title,
    film.description,
    language.name AS language_name
FROM language
    LEFT JOIN film ON language.language_id = film.language_id;
--------------------------
--3
CREATE TABLE new_film (
    id int primary key generated always as identity,
    name VARCHAR(50)
);
--------------------------
INSERT INTO new_film (name)
VALUES ('Film A'),
    ('Film B'),
    ('Film C');
--------------------------
--4
CREATE TABLE customer_review (
    review_id int primary key generated always as identity,
    film_id int REFERENCES new_film(id) ON DELETE CASCADE,
    language_id int REFERENCES language(language_id),
    title VARCHAR(50) NOT NULL,
    score int CHECK (
        score >= 1
        AND score <= 10
    ),
    review_text TEXT,
    last_update TIMESTAMP
);
--------------------------
--5
INSERT INTO customer_review (
        film_id,
        language_id,
        title,
        score,
        review_text,
        last_update
    )
VALUES (
        (
            SELECT id
            FROM new_film
            WHERE name = 'Film A'
        ),
        (
            SELECT language_id
            FROM language
            WHERE name = 'English'
        ),
        'Greate Movie',
        10,
        'The Greatest movie of mankind, almost equal to God himself Shrek',
        NOW()
    ),
    (
        (
            SELECT id
            FROM new_film
            WHERE name = 'Film B'
        ),
        (
            SELECT language_id
            FROM language
            WHERE name = 'English'
        ),
        'Mid Movie',
        5,
        'The Middest movie of them all, the one that mids the most. Donkie will ask the entire time if the action is there yet?',
        NOW()
    ),
    (
        (
            SELECT id
            FROM new_film
            WHERE name = 'Film C'
        ),
        (
            SELECT language_id
            FROM language
            WHERE name = 'English'
        ),
        'Absolute GARBAGE',
        1,
        'Cant go lower then 1, Shrek will call this blasphemy. I hope god will forgive me',
        NOW()
    );
--------------------------
--6
-- The foreign key constraint with the film_id column in the customer_review table references the id column in the new_film table. 
-- When a film is deleted from the new_film table, 
-- any records in the customer_review table that reference that film's id will be automatically deleted as well. 
-- This is because of the cascading delete on the film_id that Ive created when creating the table.
--------------------------
-- 2)
--1
UPDATE customer_review
SET language_id = 2
WHERE film_id = 1;
UPDATE customer_review
SET language_id = 3
WHERE film_id = 2;
--------------------------
--2
-- The Fk's for customer table is the adress_id key, referencing the adress table.
-- When inserting data into the customer table, you need to ensure that the values you provide 
-- for address_id already exist in the referenced table (address). In other words, 
-- the values you insert in the customer table for address_id must match existing values in the address_id columns of the address table.
--------------------------
--3
DROP TABLE customer_review;
-- In our case it is easy to drop customer_review as it, itself dependes on other tables but if for say we try and drop languages,
-- a table that has other tables depending on information in it, we will run into a problem.
--------------------------
--4
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;
--------------------------
--5
SELECT film.film_id,
    film.title,
    film.rental_rate
FROM rental
    JOIN inventory ON rental.inventory_id = inventory.inventory_id
    JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;
--------------------------
--6
--A
SELECT film_id,
    title,
    description,
    release_year,
    rental_rate
FROM film
WHERE LOWER(description) LIKE '%sumo wrestler%'
    AND film_id IN (
        SELECT film_id
        FROM film_actor
        WHERE actor_id IN (
                SELECT actor_id
                FROM actor
                WHERE first_name = 'Penelope'
                    AND last_name = 'Monroe'
            )
    );
--------------------------
--B
SELECT film_id,
    title,
    description,
    release_year,
    length,
    rating
FROM film
WHERE rating = 'R'
    AND length < '60'
    AND film_id IN (
        SELECT film_id
        FROM film_category
        WHERE category_id IN (
                SELECT category_id
                FROM category
                WHERE LOWER(name) = 'documentary'
            )
    );
--------------------------
--C
SELECT film_id,
    title,
    description,
    release_year
FROM film
WHERE rental_rate > '4.00'
    AND film_id IN (
        SELECT film_id
        FROM inventory
        WHERE inventory_id IN (
                SELECT inventory_id
                FROM rental
                WHERE rental_id IN (
                        SELECT rental_id
                        FROM payment
                        WHERE customer_id = (
                                SELECT customer_id
                                FROM customer
                                WHERE LOWER(first_name) = 'matthew'
                                    AND LOWER(last_name) = 'mahan'
                            )
                    )
                    AND return_date > '2005-07-28'
                    AND return_date < '2005-08-01'
            )
    );
--------------------------
--D
SELECT film_id,
    title,
    description,
    release_year,
    replacement_cost
FROM film
WHERE (
        LOWER(title) LIKE '%boat%'
        OR LOWER(description) LIKE '%boat%'
    )
    AND replacement_cost > 20.00
    AND film_id IN (
        SELECT film_id
        FROM rental
        WHERE customer_id = (
                SELECT customer_id
                FROM customer
                WHERE LOWER(first_name) = 'matthew'
                    AND LOWER(last_name) = 'mahan'
            )
    );
--------------------------
-- My solution isn't great.... So this is Lise's solution
SELECT film.title,
    film.replacement_cost
FROM film
    JOIN inventory ON film.film_id = inventory.film_id
    JOIN rental ON inventory.inventory_id = rental.inventory_id
    JOIN customer ON customer.customer_id = rental.customer_id
WHERE customer.first_name = 'Matthew'
    AND customer.last_name = 'Mahan'
    AND (
        title ILIKE '%boat'
        OR description ILIKE '%boat%'
    )
ORDER BY film.replacement_cost DESC