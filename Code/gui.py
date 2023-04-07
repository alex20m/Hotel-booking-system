from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem
from PyQt6 import QtWidgets
from gui_print import GUIPrint
from gui_calender import GUICalender


class GUI(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.setWindowTitle("Reservation System")
        self.center()
        self.buttons()
        self.show()

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.setGeometry(0, 0, 400, 400)
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def buttons(self):

        label = QLabel("I want to:")
        reservation_button = QPushButton("Make a reservation")
        hotel_button = QPushButton("Print all of the hotels reservations")
        guest_button = QPushButton("Print a guests reservations")

        font = QFont()
        font.setPointSize(20)
        label.setFont(font)

        self.main_layout.addWidget(label)
        self.main_layout.addWidget(reservation_button)
        self.main_layout.addWidget(hotel_button)
        self.main_layout.addWidget(guest_button)

        reservation_button.clicked.connect(self.make_reservation)
        hotel_button.clicked.connect(self.print_hotel_reservations)
        guest_button.clicked.connect(self.print_guest_reservations)

    def make_reservation(self):
        self.calender_window = GUICalender(self.hotel)

    def print_hotel_reservations(self):
        self.print_window = GUIPrint(self.hotel, "Hotel")

    def print_guest_reservations(self):
        self.print_window = GUIPrint(self.hotel, "Guest")



