from PyQt5.QtWidgets import *


class TimeTableWindow:
    def __init__(self, base=None):
        self.createTimeTableWin = QWidget(base)

        # text widgets for the window
        self.windowHeading = QLabel('Create Time Table')                            # window Heading Text
        self.semesterLabel = QLabel('Semester')                                     # 'Semester' Text
        self.batchLabel = QLabel('Batch')                                           # 'Batch' Text
        self.timingLabel = QLabel('Batch start-timing (in 24-hours format)')        # 'Batch start-timing' Text

        # input fields of the window
        self.semesterField = QLineEdit()
        self.batchField = QLineEdit()
        self.timingField = QLineEdit()
        self.timingField.setEchoMode(QLineEdit.Password)

        # ##### layout of 'create time table' window ########
        # showing heading of the window (middle-aligned)
        self.layoutForHeading = QHBoxLayout(self.createTimeTableWin)
        self.layoutForHeading.addStretch(2)                                         # for left gaps
        self.layoutForHeading.addWidget(self.windowHeading)                         # placed in-between gaps
        self.layoutForHeading.addStretch(3)                                         # for right gaps

        # to be placed left sided (below heading)
        self.layoutForSemester = QFormLayout(self.createTimeTableWin)
        self.layoutForSemester.addRow(self.semesterLabel, self.semesterField)       # pairing label and field

        # to be placed right sided (below heading)
        self.layoutForBatch = QFormLayout(self.createTimeTableWin)
        self.layoutForBatch.addRow(self.batchLabel, self.batchField)                # pairing label and field

        # putting above (left sided and right sided) widgets into a single row
        self.secondRowWidgets = QHBoxLayout(self.createTimeTableWin)
        self.secondRowWidgets.addLayout(self.layoutForSemester)
        self.secondRowWidgets.addLayout(self.layoutForBatch)

        # showing first and second rows (vertically)
        self.wholeRows = QVBoxLayout(self.createTimeTableWin)
        self.wholeRows.addStretch(1)
        self.wholeRows.addLayout(self.layoutForHeading)                 # shows 'Heading' at the top (1st row)
        self.wholeRows.addLayout(self.secondRowWidgets)                 # shows semester and batch fields (2nd row)
        self.wholeRows.addStretch(5)

        self.createTimeTableWin.setLayout(self.wholeRows)
