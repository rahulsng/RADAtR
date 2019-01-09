import json
from pymongo import MongoClient

"""
Use the following database details to input the data to your database and its collection
You can change your database name and collection_name.
"""
db_used = "University"

"""This function should be called whenever a full new course is to be inserted into courseWiseSubjects."""

client = MongoClient('localhost', 27017)
print("Connected")
db = client.University
print(f"DB Used {db_used}")


def insert_course_and_subjects():
    collection = "courseWiseSubjects"
    course_name = input("Type the course name")
    total_semesters = int(input("Provide total semesters"))
    document = {course_name: [{str(sem_number): []} for sem_number in range(1, total_semesters + 1)]}
    for i in range(total_semesters):
        while True:
            subject = input(f"Add Subject for semester {i + 1}")
            document[course_name][i][str(i + 1)].append(subject)
            add_more = input("Any more subjects\n1.True\n2.False")
            if add_more == "2":
                break

    print(document)

    db[collection].insert(document)
    print("Inserted")
    db[collection].find()
    print("printed")


def subject_removal():
    """Define a function to remove a subject/s from given course
       of a particular semester"""


def display():
    pass


def insert_all():
    collection = "courseWiseSubjects"

    # give absolute address of the records.json file to load at once
    with open('/home/atrivedi/RADAtR/Detached/Database/records.json') as f:
        file_data = json.load(f)

    db[collection].insert(file_data)
    print("Inserted")
    print(db[collection].find())
    print("printed")


# Function Called For Testing

insert_all()