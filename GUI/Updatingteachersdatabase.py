import sys
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import *


class AddingFunctionality(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MainWindow()

    def MainWindow(self):
        self.setFixedSize(600, 400)
        self.setGeometry(300, 90, 600, 400)
        self.setWindowTitle(" UPDATION OF TEACHER'S DATABASE")

        LabelMainWindow = QLabel("PLEASE  ENTER  THE  DETAILS  OF  THE  TEACHERS", self)
        LabelMainWindow.move(120, 2)
        LabelMainWindow.setStyleSheet("font-weight: bold;"
                                      "font-family: Times New Roman ;"
                                      " color: black ; "
                                      "font-size: 10pt")
        add = QPushButton("ADD",self)
        add.move(200,350)

        # namefield

        nameField = QLabel("NAME",self)
        nameField.move(70,70)
        self.TextnameField = QTextEdit(self)
        self.TextnameField.move(250,60)
        self.TextnameField.setFixedWidth(200)
        self.TextnameField.setFixedHeight(30)

        AddNew = QPushButton("+", self)
        AddNew.move(458, 68)
        AddNew.setFixedHeight(20)
        AddNew.setFixedWidth(20)
        AddNew.clicked.connect(self.texteditclear)

        # DEPARTMENT

        nameField = QLabel("SUBJECT", self)
        nameField.move(70, 110)
        teacher_comboboxes = []
        self.department = ["DCS", "Msc.-IT", "HINDI", "MATHS", "BA"]
        self.teacher_options = QComboBox(self)
        self.teacher_options.addItems(self.department)
        self.teacher_options.move(250,110)
        self.teacher_options.setFixedWidth(200)
        AddNew2 = QPushButton("+", self)
        AddNew2.move(458, 115)
        AddNew2.setFixedHeight(20)
        AddNew2.setFixedWidth(20)
        AddNew2.clicked.connect(self.Comboboxclear)
        # teacher_comboboxes.append(teacher_options)

        #uid
        uidField = QLabel("UID", self)
        uidField.move(70, 150)
        self.TextuidField = QTextEdit(self)
        self.TextuidField.move(250, 150)
        self.TextuidField.setFixedWidth(200)
        self.TextuidField.setFixedHeight(30)

        AddNew3 = QPushButton("+", self)
        AddNew3.move(458, 155)
        AddNew3.setFixedHeight(20)
        AddNew3.setFixedWidth(20)
        AddNew3.clicked.connect(self.textedituidclear)

        # Designation
        nameField = QLabel("DESIGNATION", self)
        nameField.move(70, 190)
        teacher_comboboxes = []
        self.designation = ["PROFESSOR", "ASSISTANT PROFESSOR", "ASSOCIATE PROFESSOR"]
        self.teacher_designation = QComboBox(self)
        self.teacher_designation.addItems(self.designation)
        self.teacher_designation.move(250, 190)
        self.teacher_designation.setFixedWidth(200)
        AddNew4 = QPushButton("+", self)
        AddNew4.move(458, 195)
        AddNew4.setFixedHeight(20)
        AddNew4.setFixedWidth(20)
        AddNew4.clicked.connect(self.Comboboxdesigclear)

        # maximum lectures
        maxLectures = QLabel("MAXIMUM LECTURES", self)
        maxLectures.move(70, 230)
        self.TextmaxLectures = QTextEdit(self)
        self.TextmaxLectures.move(250, 230)
        self.TextmaxLectures.setFixedWidth(200)
        self.TextmaxLectures.setFixedHeight(30)

        AddNew5 = QPushButton("+", self)
        AddNew5.move(458, 235)
        AddNew5.setFixedHeight(20)
        AddNew5.setFixedWidth(20)
        AddNew5.clicked.connect(self.textmaxLectures)

        # min lectures
        minLectures = QLabel("MINIMUM LECTURES", self)
        minLectures.move(70, 270)
        self.TextminLectures = QTextEdit(self)
        self.TextminLectures.move(250, 270)
        self.TextminLectures.setFixedWidth(200)
        self.TextminLectures.setFixedHeight(30)

        AddNew5 = QPushButton("+", self)
        AddNew5.move(458, 275)
        AddNew5.setFixedHeight(20)
        AddNew5.setFixedWidth(20)
        AddNew5.clicked.connect(self.textminLectures)

    def texteditclear(self):
        # write the code to add the text of the text edit to the database
        self.TextnameField.clear()

    def Comboboxclear(self):
        self.teacher_options.setCurrentIndex(-1)

    def textedituidclear(self):
        # write the code to add the text of the text edit to the database
        self.TextuidField.clear()

    def Comboboxdesigclear(self):
        self.teacher_designation.setCurrentIndex(-1)

    def textmaxLectures(self):
        self.TextmaxLectures.clear()

    def textminLectures(self):
        self.TextminLectures.clear()


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()