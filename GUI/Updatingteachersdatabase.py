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
        nameField.move(70, 130)
        teacher_comboboxes = []
        self.department = ["DCS", "Msc.-IT", "HINDI", "MATHS", "BA"]
        self.teacher_options = QComboBox(self)
        self.teacher_options.addItems(self.department)
        self.teacher_options.move(250,130)
        self.teacher_options.setFixedWidth(200)
        AddNew2 = QPushButton("+", self)
        AddNew2.move(458, 135)
        AddNew2.setFixedHeight(20)
        AddNew2.setFixedWidth(20)
        AddNew2.clicked.connect(self.Comboboxclear)
        # teacher_comboboxes.append(teacher_options)

        #



    def texteditclear(self):
        # write the code to add the text of the text edit to the database
        self.TextnameField.clear()

    def Comboboxclear(self):
        self.teacher_options.setCurrentIndex(-1)


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()