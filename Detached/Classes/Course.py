from Detached.Classes.Teacher import Teacher
from Detached.Classes.Teacher import check_teacher_availability


# Course Data Structure definition
class Course:
    def __init__(self, name=None, code=None, batch=0, sem=0, start_time=0):
        self.name = name
        self.code = code
        self.batch = batch
        self.totalSemesters = sem
        self.subjects = []
        self.totalSubjects = len(self.subjects)  # so that if subject is added or removed, no need to update explicitly
        self.startingHour = start_time  # 24 Hrs.
        self.teachers = []  # what is to appended here ? Full Teacher() instance or only teacher's name

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
        for teacher in self.teachers:   # if object of Teacher class is appended above in teachers then this must change
            print(teacher)
        print()

    def update_info(self):
        self.getinfo()
        print("What is the attribute you want to update ?")
        attribute = int(input(f"1.Name\n2.Course Code\n3.Start Timing\n4.No. of Semesters\n Any other key to exit"))
        if attribute == 1:
            self.name = input("Enter New Course Name")
        elif attribute == 2:
            self.code = input("Enter New Course Code")
        elif attribute == 3:
            self.startingHour = input("Enter New Start Time(24 Hrs)")
        elif attribute == 4:
            self.totalSemesters = int(input("Enter Total Semesters"))
        else:
            return

    # To be completed
    def add_subject(self, subjects_from_subject_data_structure):
        self.subjects.append(subjects_from_subject_data_structure)

    # Almost Done
    def add_teacher(self, teacher_type_object):
        if check_teacher_availability(teacher_type_object):
            self.teachers.append(teacher_type_object.name)
            print("Added Successfully")
        else:
            print("Teacher is running out of time hence, can't be added")

    # its working depends on adding of the "Teacher"'s instance or just name in above self.teacher list
    def remove_teacher(self, teacher_name):
        if teacher_name in self.teachers:
            self.teachers.remove(teacher_name)
            print("Teacher removed ")


obj = Teacher("Manoj", "DCS", 3, "SIST", "mca-mk", 17, 13, 15)
obj.getinfo()
print(check_teacher_availability(obj))
course1 = Course("MCA", "mca", 2, 2, 10)
course1.getinfo()
course1.add_teacher(obj)
course1.getinfo()
course1.remove_teacher("Manoj")
course1.getinfo()
