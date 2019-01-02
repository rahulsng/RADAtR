# Course Data Structure definition
class Course:
    def __init__(self, name=None, code=None, batch=0, sem=0, subs=0, start_time=0):
        self.name = name
        self.code = code
        self.batch = batch
        self.totalSemesters = sem
        self.totalSubjects = subs
        self.startingHour = start_time
        self.subjects = []
        self.teachers = []

    # displaying all attributes of 'Course' object
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Start Timing: {self.startingHour} hours")
        print(f"No. of Semesters: {self.totalSemesters}")
        print(f"No. of Subjects: {self.totalSubjects}")
        print(f"Subjects:")
        for subject in self.subjects:
            print(subject)
        print(f"Teachers:")
        for teacher in self.teachers:
            print(teacher)
        print()
