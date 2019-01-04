import Detached.Global.Variables.varFile1 as Var


# Teacher Data Structure Definition
class Teacher:
    def __init__(self, name=None, dept=None, rank=0, school=None, uid=None, max_lec=0, min_lec=0, current_lec=0):
        self.name = name
        self.department = dept
        self.rank = rank
        self.school = school
        self.uID = uid
        self.maxLectures = max_lec  # per week
        self.minLectures = min_lec  # per week
        self.currentLectures = current_lec
        self.lectureSlots = [[False]*Var.maximumSlots]*Var.totalWorkingDays
        self.semestersTeaching = []  # can be a number, Courses may be different for a teacher or a list of strings
        self.subjects = []

    # function to fetch attributes and their values
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"School: {self.school}")
        print(f"Universal ID: {self.uID}")
        print(f"Maximum no. of Lectures: {self.maxLectures}")
        print(f"Minimum no. of Lectures: {self.minLectures}")
        print(f"Current Lectures: {self.currentLectures}")
        # print("Lecture Slots")        # how to show busy slots?
        print("Subjects:")
        for subject in self.subjects:
            print(subject)
        print("Teachers:")
        for semester in self.semestersTeaching:
            print(semester)
        print()

    def set_max_lectures(self, max_lectures):
        if max_lectures < self.minLectures:
            print("Cannot be less than minimum lectures")
        else:
            self.maxLectures = max_lectures


# Here first argument "Teacher" (the class name) is passed to verify the given teacher's credentials
# Also so that the first argument is of Teacher's instance
def check_teacher_availability(Teacher):
        if Teacher.currentLectures < Teacher.maxLectures:
            return True
        else:
            return False
