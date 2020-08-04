import sqlite3


class Student():

    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is in {self.cohort}."


class Instructor():

    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is the instructor for {self.cohort}."


class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Exercise():

    def __init__(self, title, language):
        self.title = title
        self.langauge = language

    def __repr__(self):
        return f'{self.langauge} - {self.title}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/tannerb9/workspace/python/student_exercises/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.student_id,
                s.first_name,
                s.last_name,
                s.slack,
                s.cohort_id,
                c.name
            from students s
            join cohorts c on s.cohort_id = c.cohort_id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT * FROM cohorts
                """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT * FROM exercises
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def js_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT * FROM exercises e WHERE e.language = "JavaScript"
            """)

            javascript_exercises = db_cursor.fetchall()

            for exercise in javascript_exercises:
                print(exercise)

    def python_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT * FROM exercises e WHERE e.language = "Python"
            """)

            python_exercises = db_cursor.fetchall()

            for exercise in python_exercises:
                print(exercise)

    def cohort_instructors(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT i.instructor_id,
                i.first_name,
                i.last_name,
                i.slack,
                i.cohort_id,
                c.name
                FROM instructors i
                JOIN cohorts c ON i.cohort_id = c.cohort_id 
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.js_exercises()
reports.python_exercises()
reports.cohort_instructors()
