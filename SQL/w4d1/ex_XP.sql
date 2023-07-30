-- EX XP

-- 1)

create table items (
	id serial primary key,
	item varchar(50),
	price int,
);

create customers (
	id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
);

insert into items (item, price) values
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

insert into customers (first_name, last_name) values
('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');

select * from items;

select * from items where price > 80;

select * from items where price <= 300;

select * from customers where last_name = 'Smith';

select * from customers where last_name = 'Jones';

select * from customers where first_name != 'Scott';


-- EX XP +

-- 1)

create table students (
 id serial primary key,
 first_name varchar(50),
 last_name varchar(50),
 birth_date date
);

insert into students (first_name, last_name, birth_date)
values
    ('Marc', 'Benichou', '1998-11-02'),
    ('Yoan', 'Cohen', '2010-12-03'),
    ('Lea', 'Benichou', '1987-07-27'),
    ('Amelia', 'Dux', '1996-04-07'),
    ('David', 'Grez', '2003-06-14'),
    ('Omer', 'Simpson', '1980-10-03'),
    ('Daniel', 'Shmidet', '1998-01-08');

select * from students;

select first_name, last_name from students;

select first_name, last_name from students where id = 2;

select first_name, last_name from students 
where last_name = 'Benichou' and first_name = 'Marc';

select first_name, last_name from students 
where last_name = 'Benichou' or first_name = 'Marc';

select * from students where first_name like '%a%';

select * from students where first_name like 'A%'; -- I assume you mean capital letter A because if it's a lower case one, there is none in this table as the names start with a capital letter

select * from students where first_name like '%a';

select * from students where substring(first_name, length(first_name) - 1, 1) = 'a';

select * from students where id = 1 and id = 3;

select * from students where birth_date >= '2000-01-01';

-- This is for the daily challange, as I dont have a actors table I can use the students table to achive the same results

-- Daily challange

-- 1)

select count(*) as total_studens from students;


-- 2)

-- When you try to add a new student with some blank fields (i.e., NULL values), 

-- the outcome will depend on the table's schema and the constraints applied to the columns.

-- If the table allows NULL values for all columns and there are no constraints that restrict the insertion of NULL values, 

-- the new student will be added without any issues, and the blank fields will be stored as NULL.

-- If the table has some columns with NOT NULL constraints (meaning those columns cannot have NULL values), 

-- and you attempt to insert a new student with blank fields for those columns, 

-- the insertion will fail with an error indicating that you are violating the NOT NULL constraint.

-- For example, if first_name and last_name columns have NOT NULL constraints, 

-- and you try to add a new student with blank values for these columns, the insertion will fail.


-- EX XP Gold

-- 1)

select first_name, last_name, birth_date from students
order by last_name
limit 4;

select first_name, last_name, birth_date from students
order by birth_date desc
limit 1;

select first_name, last_name, birth_date from students
order by id
limit 3 offset 2;