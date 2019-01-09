import json
from pymongo import MongoClient
from Detached.Global.Variables.varDB import *

"""This function should be called for creating a subject list for a new course."""

client = MongoClient(localhost)
db = client[database]


def insert_course_and_subjects():
    course_name = input("Type the course name")
    total_semesters = int(input("Provide total semesters"))

    # creating an empty data structure for storing subjects
    document = {course_name: [{str(sem_number): []} for sem_number in range(1, total_semesters + 1)]}

    # adding subjects in required empty lists
    for i in range(total_semesters):
        while True:
            subject = input(f"Add Subject for semester {i + 1}")
            document[course_name][i][str(i + 1)].append(subject)
            add_more = input("Any more subjects\n1.True\n2.False")
            if add_more == "2":
                break

    db[collection].insert(document)
    db[collection].find()


def subject_removal():
    """Define a function to remove a subject/s from given course
       of a particular semester"""


def display():
    pass


def insert_all():
    # give absolute address of the records.json file to load at once
    with open('/home/atrivedi/RADAtR/Detached/Database/records.json') as f:
        file_data = json.load(f)

    db[collection].insert(file_data)
    print(db[collection].find())


# Function Called For Testing

insert_all()
