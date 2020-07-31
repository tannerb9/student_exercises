-- PRAGMA foreign_keys;

DELETE FROM cohorts;
DELETE FROM instructors;
DELETE FROM students;
DELETE FROM languages;
DELETE FROM exercises;


DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS exercises;

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

CREATE TABLE languages
(
  languageId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  language TEXT NOT NULL UNIQUE
);

CREATE TABLE exercises (
  exerciseId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  student_id INTEGER NOT NULL,
  language_id INTEGER NOT NULL,
  FOREIGN KEY
(student_id) REFERENCES students
(student_id),
  FOREIGN KEY
(language_id) REFERENCES languages
(language_id)

);
