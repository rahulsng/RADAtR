"""
    author: Anchal Aithani
    created: 30th Dec, 18

    last edit: 10th Jan, 19
    author: Dev Vrat Singh
"""

import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_main_window()         # creates Menu in the window
        self.draw_menu()
        self.draw_statusbar()
        self.draw_main_container()

    def draw_main_window(self):
        # main window properties
        self.setFixedSize(800, 600)
        self.setWindowTitle('Main Window')

    def draw_menu(self):
        menubar = QMenuBar(self)

        # adding Menu Tabs
        applicatonTab = menubar.addMenu('Application')
        aboutTab = menubar.addMenu('About')
        helpTab = menubar.addMenu('Help')

    def draw_statusbar(self):
        self.statusBar().showMessage('This is a status bar.')

    def draw_main_container(self):
        container = QWidget(self)
        container.setGeometry(0, 21, 800, 558)      # 21x2 px is taken by menu(top) and status bar(bottom)
        # container.setStyleSheet('border:0px solid black;\
        #                         background-color: rgb(45, 57, 63);')
        self.draw_rest(container)

    def draw_rest(self, base_widget):
        layout = QHBoxLayout(base_widget)

        # left most (vertical) toggle bar
        left_bar = QWidget(base_widget)
        left_bar.setMaximumWidth(30)                # static value, need not to be changed
        # left_bar.setStyleSheet('border-right: 1px solid #4B4B4B;')

        # navigation
        nav = QTreeWidget(base_widget)
        nav.setMaximumWidth(200)                    # static value to be changed with main window size

        # ########## navigation options must be defined below #############
        nav.setHeaderLabel('Time-Table')

        # right sided container for other dynamic widgets
        sub_container = QWidget(base_widget)
        # sub_container.setStyleSheet('background-color: #2B2B2B')

        layout.addWidget(left_bar)
        layout.addWidget(nav)
        layout.addWidget(sub_container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # layout.addStretch(2)
        base_widget.setLayout(layout)


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
