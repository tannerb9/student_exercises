class Student:

    def __init__(self, first_name, last_name, slack):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.exercises = []

    def show_assignments(self):
        print(f"{self.first_name} has to do the following exercises:")
        for exercise in self.exercises:
            print(f"    * {exercise.name}")
