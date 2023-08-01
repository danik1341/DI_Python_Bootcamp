-- Daily
-- 1)
--1
CREATE TABLE customer (
    id int primary key generated always as identity,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
--------------------------
CREATE TABLE customer_profile (
    id int primary key generated always as identity,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id int UNIQUE REFERENCES customer (id)
);
--------------------------
--2
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
    ('Jerome', 'Lalu'),
    ('Lea', 'Rive');
--------------------------
--3
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
        'TRUE',
        (
            SELECT id
            FROM customer
            WHERE first_name = 'John'
        )
    ),
    (
        'FALSE',
        (
            SELECT id
            FROM customer
            WHERE first_name = 'Jerome'
        )
    );
--------------------------
--4
SELECT customer.first_name
FROM customer
    JOIN customer_profile ON customer.id = customer_profile.id
WHERE customer_profile.isLoggedIn = TRUE;
--------------------------
SELECT customer.first_name,
    customer_profile.isLoggedIn
FROM customer
    LEFT JOIN customer_profile ON customer.id = customer_profile.id;
--------------------------
SELECT COUNT(*) AS not_logged
FROM customer_profile
WHERE isLoggedIn = FALSE;
--------------------------
-- 2)
--1
CREATE TABLE book (
    book_id int primary key generated always as identity,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL
);
--------------------------
--2
INSERT INTO book (title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To kill a mockingbird', 'Harper Lee');
--------------------------
--3
CREATE TABLE student (
    student_id int primary key generated always as identity,
    name VARCHAR(50) UNIQUE NOT NULL,
    age int CHECK (age <= 15)
);
--------------------------
--4
INSERT INTO student (name, age)
VALUES ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14);
--------------------------
--5
CREATE TABLE library (
    book_fk_id int REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id int REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowrd_date DATE
);
--------------------------
--6
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
        (
            SELECT book_id
            FROM book
            WHERE title = 'Alice In Wonderland'
        ),
(
            SELECT student_id
            FROM student
            WHERE name = 'John'
        ),
        '15-02-2022'
    ),
    (
        (
            SELECT book_id
            FROM book
            WHERE title = 'To kill a mockingbird'
        ),
        (
            SELECT student_id
            FROM student
            WHERE name = 'Bob'
        ),
        '2021-03-03'
    ),
    (
        (
            SELECT book_id
            FROM book
            WHERE title = 'Alice In Wonderland'
        ),
        (
            SELECT student_id
            FROM student
            WHERE name = 'Lera'
        ),
        '2021-05-23'
    ),
    (
        (
            SELECT book_id
            FROM book
            WHERE title = 'Harry Potter'
        ),
        (
            SELECT student_id
            FROM student
            WHERE name = 'Bob'
        ),
        '2021-08-12'
    );
--------------------------
--7
SELECT *
FROM library;
--------------------------
SELECT student.name AS student_name,
    book.title AS book_title
FROM library
    JOIN student ON library.student_fk_id = student.student_id
    JOIN book ON library.book_fk_id = book.book_id;
SELECT AVG(age) AS average_age
FROM student
WHERE student_id IN (
        SELECT student_fk_id
        FROM library
        WHERE book_fk_id IN (
                SELECT book_id
                FROM book
                WHERE title = 'Alice In Wonderland'
            )
    );
--------------------------
--8
DELETE FROM student
WHERE student_id = your_student_id;
-- When you delete a student from the Student table, 
-- the corresponding rows in the library junction table where the student is referenced as 
-- student_fk_id will be deleted as well. This is due to the ON DELETE CASCADE constraint on 
-- the foreign key student_fk_id in the library table, which specifies that when a related row in the Student table is deleted, 
-- the corresponding rows in the library table should also be deleted.