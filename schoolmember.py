class SchoolMember:

    def __init__(self, first_name, last_name, slack):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack


class Instructor(SchoolMember):

    def __init__(self, first_name, last_name, slack, specialty):
        super().__init__(first_name, last_name, slack)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)


class Student(SchoolMember):

    def __init__(self, first_name, last_name, slack):
        super().__init__(first_name, last_name, slack)
        self.exercises = []

    def show_assignments(self):
        print(f"{self.first_name} has to do the following exercises:")
        for exercise in self.exercises:
            print(f"    * {exercise.name}")
