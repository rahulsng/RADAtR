"""
    author: Anchal Aithani
    created: 30th Dec, 18

    last edit: 10th Jan, 19
    author: Dev Vrat Singh
"""

import sys
from GUI.ModulePanel import *


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

        # left most (vertical) toggle bar
        self.someVar = LeftModulePanel(self.container)
        self.someVar.timeTableButton.clicked.connect(self.toggle_nav)

        # navigation properties
        self.timeTableNav = QTreeWidget()
        self.timeTableNav.setMaximumWidth(200)                    # static value to be changed with main window size

        # ########## navigation options must be defined below #############
        self.timeTableNav.setHeaderLabel('Time-Table')

        # right sided container for other dynamic widgets
        self.sub_container = QWidget(self.container)
        # sub_container.setStyleSheet('background-color: #2B2B2B')

        # stacking all widgets on the main widget (ie container)
        self.containerLayout.addWidget(self.someVar.left_bar)
        self.containerLayout.addWidget(self.timeTableNav)
        self.containerLayout.addWidget(self.sub_container)
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.containerLayout.setSpacing(0)
        self.container.setLayout(self.containerLayout)

    # function to show/hide "Time-Table" (navigation) bar
    def toggle_nav(self):
        status = self.timeTableNav.isHidden()
        if status is False:
            self.timeTableNav.hide()
        else:
            self.timeTableNav.show()


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
