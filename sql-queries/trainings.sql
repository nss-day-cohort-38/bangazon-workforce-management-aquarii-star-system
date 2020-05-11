-- SQLite
-- Seeding Training
-- DROP TABLE hrapp_training_program;

-- CREATE TABLE hrapp_trainingprogram (
--   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--   title TEXT NOT NULL,
--   description TEXT NOT NULL,
--   start_date DATE NOT NULL,
--   end_date DATE NOT NULL,
--   capacity INTEGER NOT NULL
-- );
DROP TABLE hrapp_department;
CREATE TABLE hrapp_department 
  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, dept_name, budget);

INSERT INTO hrapp_department
(dept_name, budget)
VALUES
('Customer Service', 20000.00), ('Marketing', 40000.00), ('Engineering', 50000.00);

INSERT INTO hrapp_trainingprogram 
  (title, description, start_date, end_date, capacity) 
VALUES
  ("SQL For Beginners", "DESCRIPTION", "2020-05-07", "2020-10-10", 5),
  ("Django", "DESCRIPTION", "2020-01-01", "2020-02-01", 10),
  ("Cooking for Beginners", "DESCRIPTION", "2020-02-01", "2020-10-01", 11);

-- DROP TABLE hrapp_employee_training_program;
-- CREATE TABLE hrapp_employeetrainingprogram (
--   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--   training_program_id INTEGER NOT NULL,
--   employee_id INTEGER NOT NULL,
--   FOREIGN KEY (training_program_id) REFERENCES hrapp_training_program (id),
--   FOREIGN KEY (employee_id) REFERENCES hrapp_employee (id)
-- );

-- MODEL TESTING 
SELECT
    tp.id,
    tp.title,
    tp.start_date,
    tp.end_date,
    tp.capacity
FROM hrapp_training_program tp;

-- MAKING SOME EMPLOYEES
INSERT INTO hrapp_employee
  (first_name, last_name, start_date, is_supervisor)
VALUES
  ("Darby", "Ross", "2019-05-07", True),
  ("Nina", "Dale", "2020-01-01", False),
  ("Dingo", "Taller", "2020-05-07", False);

-- SEEDING EMPLOYEE TRAININGS
INSERT INTO hrapp_employeetrainingprogram
  (training_program_id, employee_id)
VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (2, 2),
  (2, 1),
  (3, 1);