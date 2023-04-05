from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem
from PyQt6 import QtWidgets
from hotel import Hotel




class GUIPrint(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()

        self.setWindowTitle("Hotels reservations")

        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.print_hotel()

        self.showMaximized()

    def print_hotel(self):
        print(Hotel.read_previous_reservations())

    def print_guest(self):
        pass
