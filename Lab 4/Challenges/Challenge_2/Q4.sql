ALTER TABLE grades
ADD student_name VARCHAR(100);

UPDATE grades
INNER JOIN students
ON grades.student_id = students.id
SET grades.student_name = students.name;
Select * from grades;