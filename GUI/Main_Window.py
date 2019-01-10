"""
    author: Anchal Aithani
    created: 30th Dec, 18

    last edit: 10th Jan, 19
    author: Dev Vrat Singh
"""

import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon       # for importing icon
from PyQt5.QtCore import QSize      # for icon size


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties
        self.setFixedSize(800, 600)
        self.setWindowTitle('Main Window')

        # menu bar settings
        self.menuBar = QMenuBar(self)

        # adding Menu Tabs
        self.applicationTab = self.menuBar.addMenu('Application')
        self.aboutTab = self.menuBar.addMenu('About')
        self.helpTab = self.menuBar.addMenu('Help')

        # status bar properties
        self.statusBar().showMessage('This is a status bar.')

        # central widget (main parent widget)
        self.container = QWidget(self)
        self.container.setGeometry(0, 21, 800, 558)      # 21x2 px is taken by menu(top) and status bar(bottom)
        # container.setStyleSheet('border:0px solid black;\
        #                         background-color: rgb(45, 57, 63);')

        # layout for main widget (container)
        self.containerLayout = QHBoxLayout(self.container)

        # navigation properties
        self.nav = QTreeWidget()
        self.nav.setMaximumWidth(200)                    # static value to be changed with main window size

        # ########## navigation options must be defined below #############
        self.nav.setHeaderLabel('Time-Table')

        # left most (vertical) toggle bar
        self.left_bar = QWidget(self.container)
        self.left_bar.setMaximumWidth(50)                # static value, need not to be changed

        # layout for left bar
        self.leftBarLayout = QVBoxLayout(self.left_bar)

        # buttons on the left bar
        self.timetablebutton = QPushButton('', self.left_bar)
        self.timetablebutton.setIcon(QIcon('GUI/Icons/timetable.png'))
        self.timetablebutton.setIconSize(QSize(40, 40))
        self.timetablebutton.clicked.connect(self.toggle_nav)

        # stacking all buttons in left bar
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.timetablebutton)
        self.leftBarLayout.addStretch(20)
        self.leftBarLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBarLayout.setSpacing(0)
        self.left_bar.setLayout(self.leftBarLayout)

        # right sided container for other dynamic widgets
        self.sub_container = QWidget(self.container)
        # sub_container.setStyleSheet('background-color: #2B2B2B')

        # stacking all widgets on the main widget (ie container)
        self.containerLayout.addWidget(self.left_bar)
        self.containerLayout.addWidget(self.nav)
        self.containerLayout.addWidget(self.sub_container)
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.containerLayout.setSpacing(0)
        self.container.setLayout(self.containerLayout)

    # function to show/hide "Time-Table" (navigation) bar
    def toggle_nav(self):
        status = self.nav.isHidden()
        if status is False:
            self.nav.hide()
        else:
            self.nav.show()


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
