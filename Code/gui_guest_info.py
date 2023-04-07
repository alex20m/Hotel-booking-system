from PyQt6.QtCore import QRegularExpression, Qt, QDate
from PyQt6.QtGui import QFont, QTextCharFormat, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit, QComboBox
from PyQt6 import QtWidgets
from hotel import Hotel
from datetime import date, timedelta, datetime
from guest import Guest
from reservations import Reservations



class GUIGuestInfo(QtWidgets.QMainWindow):

    def __init__(self, hotel, room_type, price, start_date, end_date):
        super().__init__()
        self.setWindowTitle("Customer info")

        self.hotel = hotel
        self.room_type = room_type
        self.price = price
        self.start_date = start_date
        self.end_date = end_date

        self.name = None
        self.email = None
        self.phone_nr = None
        self.comments = None

        self.font = QFont()
        self.font.setPointSize(26)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.info_layout = QVBoxLayout()
        self.name_layout = QHBoxLayout()
        self.phone_layout = QHBoxLayout()
        self.email_layout = QHBoxLayout()
        self.comments_layout = QHBoxLayout()

        self.info_layout.addLayout(self.name_layout)
        self.info_layout.addLayout(self.phone_layout)
        self.info_layout.addLayout(self.email_layout)
        self.info_layout.addLayout(self.comments_layout)

        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.make_info()
        self.confirmation()

        self.showMaximized()

    def make_info(self):

        name_label = QLabel("Enter your name:")
        self.name_layout.addWidget(name_label)
        name_input = QLineEdit()
        self.name_layout.addWidget(name_input)
        name_label.setFont(self.font)

        phone_label = QLabel("Enter your phone number:")
        self.phone_layout.addWidget(phone_label)
        phone_input = QLineEdit()
        self.phone_layout.addWidget(phone_input)
        phone_label.setFont(self.font)

        email_label = QLabel("Enter your email:")
        self.email_layout.addWidget(email_label)
        email_input = QLineEdit()
        self.email_layout.addWidget(email_input)
        email_label.setFont(self.font)

        comments_label = QLabel("Do you have any additional comments?")
        self.comments_layout.addWidget(comments_label)
        comments_input = QLineEdit()
        self.comments_layout.addWidget(comments_input)
        comments_label.setFont(self.font)


        self.main_layout.addLayout(self.info_layout)

    def confirmation(self):
        font = QFont()
        font.setPointSize(40)

        self.confirmation_label = QLabel("Confirm reservation")
        self.main_layout.addWidget(self.confirmation_label)
        self.confirmation_label.setFont(font)
        self.confirmation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.confirmation_layout = QHBoxLayout()
        self.main_layout.addLayout(self.confirmation_layout)

        self.room_label = QLabel("Room type: " + str(self.room_type))
        self.room_label.setFont(self.font)
        self.start_label = QLabel("Check-in: " + str(self.start_date))
        self.start_label.setFont(self.font)
        self.end_label = QLabel("Check-out: " + str(self.end_date))
        self.end_label.setFont(self.font)
        self.price_label = QLabel("Price of stay: {}€".format(self.price))
        self.price_label.setFont(self.font)

        self.confirmation_layout.addWidget(self.room_label)
        self.confirmation_layout.addWidget(self.start_label)
        self.confirmation_layout.addWidget(self.end_label)
        self.confirmation_layout.addWidget(self.price_label)

        self.confirmation_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        button = QPushButton("Reserve room")
        button.setFont(font)
        self.main_layout.addWidget(button)






