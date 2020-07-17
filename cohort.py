class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []

    def addStudents(self, *students):
        for student in students:
            self.students.append(student)

    def addInstructors(self, *instructors):
        for instructor in instructors:
            self.instructors.append(instructor)
