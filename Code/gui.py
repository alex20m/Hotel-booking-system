from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QGraphicsRectItem


class GUI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.calender_layout = QVBoxLayout()

        self.main_layout.addLayout(self.calender_layout)

        self.calender = QCalendarWidget()

        self.calender_layout.addWidget(self.calender)
        self.main_widget.setLayout(self.main_layout)

        self.setWindowTitle("Reservation System")
        self.showMaximized()






