from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon       # for importing icon
from PyQt5.QtCore import QSize      # for icon size


class LeftModulePanel:
    def __init__(self, base=None):

        # left most (vertical) toggle bar
        self.left_bar = QWidget(base)
        self.left_bar.setMaximumWidth(50)                # static value, need not to be changed

        # layout for left bar
        self.leftBarLayout = QVBoxLayout(self.left_bar)

        # buttons on the left bar
        self.timeTableButton = QPushButton('', self.left_bar)
        self.timeTableButton.setIcon(QIcon('Icons/timetable.png'))
        self.timeTableButton.setIconSize(QSize(40, 40))
        # self.timeTableButton.clicked.connect(self.toggle_nav)

        # stacking all buttons in left bar
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.timeTableButton)
        self.leftBarLayout.addStretch(20)
        self.leftBarLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBarLayout.setSpacing(0)
        self.left_bar.setLayout(self.leftBarLayout)
