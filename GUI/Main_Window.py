import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.WidgetsUsed()

    def WidgetsUsed(self):
        # creating a horizontal layout for navigation panel, main frame and info panel
        Hbox = QHBoxLayout(self)

        # StyledPanel is used to create a rectangular panel
        Topleft = QFrame()
        Topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # adds the navigation panel and main frame in Splitter1
        Splitter1 = QSplitter(Qt.Horizontal)
        Textedit = QTextEdit()
        Splitter1.addWidget(Topleft)
        Splitter1.addWidget(Textedit)
        Splitter1.setSizes([100, 200])

        # adding Spitter1 and the info panel int the Splitter2
        Splitter2 = QSplitter(Qt.Vertical)
        Splitter2.addWidget(Splitter1)
        Splitter2.addWidget(bottom)
        Splitter2.setSizes([6, 8])
        # Splitter2.setEnabled(False)

        Hbox.addWidget(Splitter2)

        self.setGeometry(200, 200, 1000, 1000)
        self.setWindowTitle('Main Window')
        self.show()


def main():
    QApplicationObj = QApplication(sys.argv)
    MainWindowObj = MainWindow()
    sys.exit(QApplicationObj.exec_())


if __name__ == '__main__':
    main()
