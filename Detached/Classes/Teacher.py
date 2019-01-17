import json
import Detached.Global.Variables.varFile1 as Var
from pymongo import MongoClient
from Detached.Global.Variables.varDB import *

client = MongoClient(localhost)
db = client[database]

"""The subjects attribute that is provided in the class will be a list of dictionaries which will 
    contain semester number as their keys and "list" of subjects as their values, 
    as an example of this attribute is given in the teachers.json file.
"""


# Teacher Data Structure Definition
class Teacher:
    def __init__(self, name=None, dept=None, rank=None, school=None, uid=None, max_lec=None, min_lec=None,
                 sem_taught=None):
        self.name = name
        self.department = dept
        self.rank = rank
        self.school = school
        self.uID = uid  # String
        self.maxLectures = max_lec  # per week
        self.minLectures = min_lec  # per week
        self.lectureSlots = [[False] * Var.maximumSlots] * Var.totalWorkingDays
        self.semestersTeaching = sem_taught
        self.subjects = []  # self.add_subjects_for_teachers()

    # function to fetch attributes and their values
    def getinfo(self):

        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"School: {self.school}")
        print(f"Universal ID: {self.uID}")
        print(f"Maximum no. of Lectures: {self.maxLectures}")
        print(f"Minimum no. of Lectures: {self.minLectures}")
        # print("Lecture Slots")        # how to show busy slots?
        print("Subjects:")
        print("Teachers:")
        for semester in self.semestersTeaching:
            print(semester)
        print()

    def set_max_lectures(self, max_lectures):
        if max_lectures < self.minLectures:
            print("Cannot be less than minimum lectures")
        else:
            self.maxLectures = max_lectures

    def update_info(self):
        pass

    def add_teacher(self):
        document = {"name": self.name, "department": self.department, "school": self.school, "uid": self.uID,
                    "rank": self.rank, "max_l": self.maxLectures, "min_l": self.minLectures,
                    "semester_teaching": [{self.department: self.semestersTeaching}],
                    "subjects": self.subjects,
                    "empty_slots": [{day: list(str(x) for x in range(1, 7))} for day in Var.days_list]
                    }

        db[teacher_collection].insert(document)
        print("data inserted")

    """def add_subjects_for_teachers(self):
        total_semester = int(input("How many semesters does this course have to teach ?"))
        subject_list = [{str(sem_no): []} for sem_no in range(1, total_semester+1)]
        for i in range(total_semester):
            while True:
                subject = input(f"Enter the subject to be taught by {self.name} in semester{i + 1}")
                subject_list[i][str(i+1)].append(subject)
                add_more = input("Any more subjects in this semester\n1.True\n2.False")
                if add_more == "2":
                    break
        print(subject_list)
        return subject_list"""


# Here first argument "Teacher" (the class name) is passed to verify the given teacher's credentials
# Also so that the first argument is of Teacher's instance
def check_teacher_availability(teacher_uid):
    details = get_details(teacher_uid)
    pass


# Function to get details of the teacher for a given uID
def get_details(uid):
    return db[teacher_collection].find({"uid": uid})


def load_teachers_at_once():
    with open("/home/atrivedi/RADAtR/Detached/Database/teachers.json") as f:
        file_data = json.load(f)

    db[teacher_collection].insert(file_data)


"""To load teachers at once uncomment below line """
load_teachers_at_once()
# check_teacher_availability("None")

# This is given for example
obj = Teacher("Sanjay Kumar Dwivedi", "DCS", "1", "SIST", uid="21130", max_lec=15, min_lec=13,
              sem_taught={"MCA": ["2", "3", "4", "5"]})
obj.add_teacher()
print("done")

cursor = get_details("21130")

for values in cursor:
    print(values)

