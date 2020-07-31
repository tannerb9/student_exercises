# DELETE FROM cohorts;
# DELETE FROM instructors;
# DELETE FROM students;
# DELETE FROM languages;
# DELETE FROM exercises;
# DELETE FROM student_exercises;

# DROP TABLE IF EXISTS cohorts;
# DROP TABLE IF EXISTS instructors;
# DROP TABLE IF EXISTS students;
# DROP TABLE IF EXISTS languages;
# DROP TABLE IF EXISTS exercises;
# DROP TABLE IF EXISTS student_exercises;


# CREATE TABLE cohorts (
#   cohort_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL UNIQUE
# );

# CREATE TABLE instructors (
#   instructor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   slack TEXT UNIQUE,
#   specialty TEXT,
#   cohort_id INTEGER NOT NULL,
#   FOREIGN KEY
# (cohort_id) REFERENCES cohorts
# (cohort_id)
# );

# CREATE TABLE students (
#   student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   slack TEXT UNIQUE,
#   cohort_id INTEGER NOT NULL,
#   FOREIGN KEY
# (cohort_id) REFERENCES cohorts
# (cohort_id)
# );

# CREATE TABLE languages
# (
#   language_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   language TEXT NOT NULL
# );


# CREATE TABLE exercises (
#   exercise_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   language_id TEXT NOT NULL,
#   FOREIGN KEY
# (language_id) REFERENCES languages
# (language_id)
# );

# CREATE TABLE student_exercises
# (
#   student_exercise_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#   student_id INTEGER NOT NULL,
#   exercise_id INTEGER NOT NULL,
#   FOREIGN KEY
# (student_id) REFERENCES students
# (student_id),
#   FOREIGN KEY
# (exercise_id) REFERENCES exercises
# (exercise_id)
# );

# INSERT INTO cohorts
#   (name)
# VALUES
#   ("Cohort 40");

# INSERT INTO cohorts
#   (name)
# VALUES
#   ("Cohort 41");

# INSERT INTO cohorts
#   (name)
# VALUES
#   ("Cohort 42");

# INSERT INTO languages
#   (language)
# VALUES
#   ("Python");

# INSERT INTO languages
#   (language)
# VALUES
#   ("JavaScript");

# INSERT INTO languages
#   (language)
# VALUES
#   ("C#");

# INSERT INTO exercises
#   (null,
# title)
# VALUES
#   ("Dictionaries");

# INSERT INTO exercises
# SELECT NULL, "Dictionaries", l.language_id
# FROM exercises e, languages l
# WHERE
