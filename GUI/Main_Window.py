"""
    author: Anchal Aithani
    created: 30th Dec, 18

    last edit: 1st Dec, 19
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
        self.setFixedSize(1280, 720)
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
        central_widget = QWidget(self)
        central_widget.setGeometry(0, 25, 1260, 710)

        # StyledPanel is used to create a rectangular panel
        nav = QFrame()
        nav.setFrameShape(QFrame.StyledPanel)
        nav.setMinimumWidth(200)
        nav.setMaximumWidth(400)
        nav.setStyleSheet('background-color: rgba(0, 0, 0, 0.5)')

        content_area = QWidget(central_widget)
        content_area.setFixedHeight(600)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        bottom.setStyleSheet('border: 1px solid white')
        # bottom.

        # adds the navigation panel and main frame in Splitter1
        Splitter1 = QSplitter(Qt.Horizontal)
        Splitter1.addWidget(nav)
        Splitter1.addWidget(content_area)
        Splitter1.setSizes([80, 220])

        # creating a vertical layout for splitter1 and info panel
        v_box = QVBoxLayout(central_widget)
        v_box.addWidget(Splitter1)
        v_box.addWidget(bottom)


def main():
    application = QApplication(sys.argv)
    mainWindowObj = MainWindow()
    mainWindowObj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
