from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QPalette, QBrush, QGuiApplication, QScreen
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem
from PyQt6 import QtWidgets

from gui_remove import GUIRemove
from gui_print import GUIPrint
from gui_calender import GUICalender


class GUI(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel

        self.pixmap = QPixmap("image.jpeg")
        self.palette = self.palette()
        self.palette.setBrush(QPalette.ColorRole.Window, QBrush(self.pixmap.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)))
        self.setPalette(self.palette)

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
        self.setGeometry(0, 0, 640, 480)
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def buttons(self):

        label = QLabel("Alex Hotel")
        reservation_button = QPushButton("Make a reservation")
        hotel_button = QPushButton("Print the hotels reservations")
        guest_button = QPushButton("Print a guests reservations")
        remove_button = QPushButton("Remove a reservation")

        reservation_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.7)")
        hotel_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.7)")
        guest_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.7)")
        remove_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.7)")

        font = QFont("Brush Script MT", 100)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setStyleSheet("color: black")

        self.main_layout.addSpacing(80)
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(reservation_button)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(hotel_button)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(guest_button)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(remove_button)

        reservation_button.clicked.connect(self.make_reservation)
        hotel_button.clicked.connect(self.print_hotel_reservations)
        guest_button.clicked.connect(self.print_guest_reservations)
        remove_button.clicked.connect(self.remove_reservation)

    def make_reservation(self):
        self.calender_window = GUICalender(self.hotel)

    def print_hotel_reservations(self):
        self.print_window = GUIPrint(self.hotel, "Hotel")

    def print_guest_reservations(self):
        self.print_window = GUIPrint(self.hotel, "Guest")

    def remove_reservation(self):
        self.remove_window = GUIRemove(self.hotel)

    def resizeEvent(self, event):
        self.palette.setBrush(QPalette.ColorRole.Window, QBrush(self.pixmap.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)))
        self.setPalette(self.palette)


