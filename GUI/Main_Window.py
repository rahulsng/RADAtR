"""
    author: Anchal Aithani
    created: 30th Dec, 18

    last edit: 31st Dec, 18
    author: Dev Vrat Singh
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawMenu()       # creates Menu in the window
        self.drawFrames()

    # dummy function
    def someAction(self):
        pass

    # function which creates all interface
    def drawMenu(self):
        # main window properties
        self.setGeometry(80, 60, 800, 600)
        self.setWindowTitle('Main Window')

        # creating Main Menu
        menu = self.menuBar()

        # adding Menu Tabs
        applicatonTab = menu.addMenu('Application')
        aboutTab = menu.addMenu('About')
        helpTab = menu.addMenu('Help')

        # ------------ Sub-menus of each Tab ---------------
        # 'Exit' (of Application) sub-menu and its properties
        applicatonTab_exit = QAction('Exit', self)
        applicatonTab_exit.setShortcut('Ctrl+Q')
        applicatonTab_exit.triggered.connect(qApp.exit)         # exit the application
        applicatonTab.addAction(applicatonTab_exit)             # adding to 'Application' Tab

        # 'Software' (Of About) sub-menu and its properties
        aboutTab_software = QAction('Software', self)
        aboutTab_software.triggered.connect(self.someAction)
        aboutTab.addAction(aboutTab_software)

        # 'Team' (Of About) sub-menu and its properties
        aboutTab_team = QAction('Team', self)
        aboutTab_team.triggered.connect(self.someAction)
        aboutTab.addAction(aboutTab_team)

    def drawFrames(self):
        """h = QHBoxLayout(central_widget)

        frame1 = QFrame(central_widget)
        frame1.setStyleSheet('border: 1px solid black')
        frame2 = QFrame(central_widget)

        h.addWidget(frame1)
        h.addWidget(frame2)

        central_widget.setLayout(h)"""


def main():
    application = QApplication(sys.argv)
    mainWindowObj = MainWindow()
    mainWindowObj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
