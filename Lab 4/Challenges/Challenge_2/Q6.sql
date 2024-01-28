UPDATE teachers
SET ContactName = 'Ramsin'
WHERE name = 'Hoover';

ALTER TABLE courses
ADD teacher_name VARCHAR(100);

UPDATE courses
INNER JOIN teachers
ON courses.teacher_id = teachers.id
SET courses.teacher_name = teachers.name;
Select * from grades;