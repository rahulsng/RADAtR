from PyQt5.QtWidgets import *


class TimeTableWindow:
    def __init__(self, base=None):
        self.createTimeTableWin = QWidget(base)

        # text widgets for the window
        self.windowHeading = QLabel('Create Time Table')                            # window Heading Text
        self.windowHeading.setStyleSheet('font-size: 16px;'
                                         'font-weight: bold;'
                                         'margin-top: 2px;'
                                         'margin-bottom: 5px;')

        self.semesterLabel = QLabel('For Semester')                                     # 'Semester' Text
        self.batchLabel = QLabel('For Batch')                                           # 'Batch' Text
        self.timingLabel = QLabel('Batch start-timing (in 24-hours format)')        # 'Batch start-timing' Text

        # input fields of the window
        self.semesterField = QLineEdit()
        self.semesterField.setFixedWidth(40)        # making input field tiny
        self.batchField = QLineEdit()
        self.batchField.setFixedWidth(40)           # making input field tiny
        self.timingField = QLineEdit()
        self.timingField.setEchoMode(QLineEdit.Password)

        # layout for rows
        self.rows = QVBoxLayout(self.createTimeTableWin)

        # form layout for semester fields (pair of label and field)
        self.semRow = QFormLayout(self.createTimeTableWin)
        self.semRow.addRow(self.semesterLabel, self.semesterField)

        # for layout for batch fields (pair of label and field)
        self.batchRow = QFormLayout(self.createTimeTableWin)
        self.batchRow.addRow(self.batchLabel, self.batchField)

        # for layout for timing fields (pair of label and field)
        self.timingRow = QFormLayout(self.createTimeTableWin)
        self.timingRow.addRow(self.timingLabel, self.timingField)

        # putting main heading in the first row
        self.firstRow = QHBoxLayout(self.createTimeTableWin)
        self.firstRow.addStretch()
        self.firstRow.addWidget(self.windowHeading)
        self.firstRow.addStretch()

        # putting semester and batch row next to each other in 2nd row
        self.secondRow = QHBoxLayout(self.createTimeTableWin)
        self.secondRow.addLayout(self.semRow, 1)
        self.secondRow.addLayout(self.batchRow, 1)

        # adding layouts and widgets into rows
        self.rows.addLayout(self.firstRow)
        self.rows.addLayout(self.secondRow)
        self.rows.addLayout(self.timingRow)
        self.rows.addStretch(5)

        self.createTimeTableWin.setLayout(self.rows)
