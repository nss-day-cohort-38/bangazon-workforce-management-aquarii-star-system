-- SQLite
-- Seeding Training, Employee Trainings

CREATE TABLE hrapp_training_program (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  capacity INTEGER NOT NULL
);

INSERT INTO hrapp_training_program 
  (title, start_date, end_date, capacity) 
VALUES
  ("SQL For Beginners", "2020-05-07", "2020-10-10", 5),
  ("Django", "2020-01-01", "2020-02-01", 10),
  ("Cooking for Beginners", "2020-02-01", "2020-10-01", 11);

CREATE TABLE hrapp_employee_training_program (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  training_program_id INTEGER NOT NULL,
  employee_id INTEGER NOT NULL,
  FOREIGN KEY (training_program_id) REFERENCES hrap_training_program (id),
  FOREIGN KEY (employee_id) REFERENCES hrap_employee (id)
);

-- MODEL TESTING 
SELECT
    tp.id,
    tp.title,
    tp.start_date,
    tp.end_date,
    tp.capacity
FROM hrapp_training_program tp;