from student import Student
from exercise import Exercise
from instructor import Instructor
from cohort import Cohort


classes_ex = Exercise("Classes", "Python")
dicts_ex = Exercise("Dictionaries", "Python")
lists_ex = Exercise("Lists", "Python")
tuples_ex = Exercise("Tuples", "Python")

cohort_forty = Cohort("Cohort 40")
cohort_thirty_nine = Cohort("Cohort 39")
cohort_thirty_eight = Cohort("Cohort 38")
cohort_forty_one = Cohort("Cohort 41")

jessie = Student("Jessie", "Mess", "messiejessie")
sam = Student("Sam", "Alama", "samalama")
tim = Student("Tim", "Tam", "timtam")
seymore = Student("Seymore", "Butts", "seybutts")

cohort_forty.addStudents(jessie)
for student in cohort_forty.students:
    print(student.first_name)

cohort_forty_one.addStudents(sam)
for student in cohort_forty_one.students:
    print(student.first_name)

cohort_thirty_eight.addStudents(tim)
for student in cohort_thirty_eight.students:
    print(student.first_name)

cohort_thirty_nine.addStudents(seymore)
for student in cohort_thirty_nine.students:
    print(student.first_name)

betty = Instructor("Betty", "Boop", "boopity", "karate")
terry = Instructor("Tare", "Ible", "taretare", "juggling")
vert = Instructor("Vert", "Eckle", "verte", "magic")

cohort_thirty_nine.addInstructors(betty)
for instructor in cohort_thirty_nine.instructors:
    print(instructor.first_name)

cohort_forty.addInstructors(terry)
for instructor in cohort_forty.instructors:
    print(instructor.first_name)

cohort_forty_one.addInstructors(vert)
for instructor in cohort_forty_one.instructors:
    print(instructor.first_name)
