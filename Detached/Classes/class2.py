# Teacher Data Structure Definition
class Teacher:
    def __init__(self, name=None, dept=None, school=None, uid=None, max_lec=0, min_lec=0):
        self.name = name
        self.department = dept
        self.school = school
        self.uID = uid
        self.maxLectures = max_lec
        self.minLectures = min_lec
        self.semestersTeaching = []
        self.subjects = []

    # function to fetch attributes and their values
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"School: {self.school}")
        print(f"Universal ID: {self.uID}")
        print(f"Maximum no. of Lectures: {self.maxLectures}")
        print(f"Minimum no. of Lectures: {self.minLectures}")
        print(f"Subjects:")
        for subject in self.subjects:
            print(subject)
        print(f"Teachers:")
        for semester in self.semestersTeaching:
            print(semester)
        print()