DELETE FROM cohorts;
DELETE FROM instructors;
DELETE FROM students;
DELETE FROM exercises;
DELETE FROM student_exercises;

DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS student_exercises;


CREATE TABLE cohorts (
  cohort_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE instructors (
  instructor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  slack TEXT UNIQUE,
  specialty TEXT,
  cohort_id INTEGER NOT NULL,
  FOREIGN KEY
(cohort_id) REFERENCES cohorts
(cohort_id)
);

CREATE TABLE students (
  student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  slack TEXT UNIQUE,
  cohort_id INTEGER NOT NULL,
  FOREIGN KEY
(cohort_id) REFERENCES cohorts
(cohort_id)
);

CREATE TABLE exercises (
  exercise_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  language TEXT NOT NULL
);

CREATE TABLE student_exercises
(
  student_exercise_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  exercise_id INTEGER NOT NULL,
  FOREIGN KEY
(student_id) REFERENCES students
(student_id),
  FOREIGN KEY
(exercise_id) REFERENCES exercises
(exercise_id)
);

INSERT INTO cohorts
  (name)
VALUES
  ("Cohort 40");

INSERT INTO cohorts
  (name)
VALUES
  ("Cohort 41");

INSERT INTO cohorts
  (name)
VALUES
  ("Cohort 42");

INSERT INTO exercises
  (title, language)
VALUES
  ("Dictionaries", "Python");
INSERT INTO exercises
  (title, language)
VALUES
  ("Lists", "Python");
INSERT INTO exercises
  (title, language)
VALUES
  ("Arrays", "JavaScript");
INSERT INTO exercises
  (title, language)
VALUES
  ("Tuples", "Python");
INSERT INTO exercises
  (title, language)
VALUES
  ("Functions", "JavaScript");

INSERT INTO instructors
SELECT NULL, "Joe", "Shepherd", "joeshep", "dad jokes", c.name
FROM cohorts c
WHERE c.name = "Cohort 40";

INSERT INTO instructors
SELECT NULL, "Lucy", "Gucy", "lgucy", "burping", c.name
FROM cohorts c
WHERE c.name = "Cohort 41";

INSERT INTO instructors
SELECT NULL, "Fire", "Cracker", "popboom", "scaring people", c.name
FROM cohorts c
WHERE c.name = "Cohort 42";

INSERT INTO students
SELECT NULL, "Joe", "Dirt", "deertay", c.name
FROM cohorts c
WHERE c.name = "Cohort 40";

INSERT INTO students
SELECT NULL, "Flo", "Rider", "floflo", c.name
FROM cohorts c
WHERE c.name = "Cohort 40";

INSERT INTO students
SELECT NULL, "Dirk", "Diggler", "diggler", c.name
FROM cohorts c
WHERE c.name = "Cohort 41";

INSERT INTO students
SELECT NULL, "Jess", "Bess", "jessie", c.name
FROM cohorts c
WHERE c.name = "Cohort 41";

INSERT INTO students
SELECT NULL, "Mira", "Till", "mtill", c.name
FROM cohorts c
WHERE c.name = "Cohort 41";

INSERT INTO students
SELECT NULL, "Jack", "Black", "jblack", c.name
FROM cohorts c
WHERE c.name = "Cohort 42";

INSERT INTO students
SELECT NULL, "Laura", "Croft", "raider", c.name
FROM cohorts c
WHERE c.name = "Cohort 42";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "diggler" AND e.title = "Dictionaries";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "diggler" AND e.title = "Lists";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "jblack" AND e.title = "Lists";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "jblack" AND e.title = "Functions";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "jessie" AND e.title = "Functions";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "jessie" AND e.title = "Functions";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "floflo" AND e.title = "Dictionaries";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "floflo" AND e.title = "Functions";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "deertay" AND e.title = "Arrays";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "deertay" AND e.title = "Lists";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "mtill" AND e.title = "Functions";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "mtill" AND e.title = "Dictionaries";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "raider" AND e.title = "Arrays";

INSERT INTO student_exercises
SELECT NULL, s.student_id, e.exercise_id
FROM students s, exercises e
WHERE s.slack = "raider" AND e.title = "Tuples";

