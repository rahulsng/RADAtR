from PyQt5.QtWidgets import *


class TimeTableWindow:
    def __init__(self, base=None):
        self.createTimeTableWin = QWidget(base)

        # dependencies
        self.teachers = ["Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]
        self.subjects = ["MCA-401", "MCA-402", "MCA-403", "MCA-404", "MCA-405"]
        self.semesterList = ["1", "2", "3", "4", "5", "6"]

        # text widgets for the window
        self.windowHeading = QLabel('Create Time Table')                            # window Heading Text
        self.windowHeading.setStyleSheet('font-size: 16px;'
                                         'font-weight: bold;'
                                         'margin-top: 2px;'
                                         'margin-bottom: 5px;')

        # input fields of the window
        self.semesterField = QComboBox()
        self.semesterField.addItems(self.semesterList)                 # list values must be passed
        self.semesterField.setFixedWidth(60)
        self.batchField = QLineEdit()
        self.batchField.setFixedWidth(60)
        self.timingField = QLineEdit()
        self.timingField.setFixedWidth(80)

        # layout for rows
        self.rows = QVBoxLayout(self.createTimeTableWin)

        # form layout for all fields (pair of label and field)
        self.semRow = QFormLayout(self.createTimeTableWin)
        self.semRow.addRow(QLabel("For Semester"), self.semesterField)
        self.semRow.addRow(QLabel("For Batch"), self.batchField)
        self.semRow.addRow(QLabel('Batch start-timing (in 24-hours format)'),
                           self.timingField)

        # putting main heading in the first row
        self.firstRow = QHBoxLayout(self.createTimeTableWin)
        self.firstRow.addWidget(self.windowHeading)
        self.firstRow.addStretch()

        # properties of the horizontal line
        self.someVar = QFrame(self.createTimeTableWin)
        self.someVar.setFrameShape(QFrame.HLine)
        self.someVar.setFrameShadow(QFrame.Sunken)

        # adding layouts and widgets into rows
        self.rows.addLayout(self.firstRow)
        self.rows.addLayout(self.semRow)
        self.rows.addStretch(1)
        self.rows.addWidget(self.someVar)       # placing horizontal line
        self.rows.addWidget(QLabel('Assign the following subjects with respective lecturer'))
        self.rows.addStretch(1)

        self.subject_mappings(self.subjects, self.teachers)
        self.rows.addStretch(10)
        self.createTimeTableWin.setLayout(self.rows)

    def subject_mappings(self, subject_list, teacher_list):
        # temporary lists
        teacher_comboboxes = []
        subject_stack = []

        if len(subject_list) >= len(teacher_list):
            index = len(teacher_list)
        else:
            index = len(subject_list)

        # creating list of lists
        for t in range(len(teacher_list)):
            teacher_options = QComboBox()
            teacher_options.addItems(teacher_list)
            teacher_comboboxes.append(teacher_options)

        for i in range(index):
            subject = QLabel(subject_list[i])
            subject_stack.append(subject)
            self.rows.addWidget(subject_stack[i])
            self.rows.addWidget(teacher_comboboxes[i])
