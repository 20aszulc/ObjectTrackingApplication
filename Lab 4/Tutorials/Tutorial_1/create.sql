--Creates a table for students
CREATE TABLE students(
    id integer  AUTO_INCREMENT primary key,
    first_name varchar(32),
    last_name varchar(32),
    email varchar(32),
    age int,
    created_at  TIMESTAMP
    );
