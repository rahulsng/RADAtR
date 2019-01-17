from Detached.Global.Configurations.ConnectionEstablishment import *
import json


# Here first argument "Teacher" (the class name) is passed to verify the given teacher's credentials
# Also so that the first argument is of Teacher's instance
def check_teacher_availability(teacher_uid):
    details = get_teacher_details(teacher_uid)
    pass


# Function to get details of the teacher for a given uID
def get_teacher_details(uid):
    return db[teacher_collection].find({"uid": uid})


def load_teachers_at_once():
    # static address of JSON file, must be updated according to one's PC
    with open("/home/dev/RADAtR/Detached/Database/teachers.json") as f:
        file_data = json.load(f)

    db[teacher_collection].insert(file_data)


"""To load all the teachers at once (from a JSON file) uncomment below line """
# load_teachers_at_once()
