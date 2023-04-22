from datetime import datetime

from PyQt6.QtCore import QRegularExpression, Qt, QDate
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit, QDateEdit, QSpacerItem, \
    QCheckBox
from PyQt6 import QtWidgets



class GUIRemove(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.label_list = []

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.setWindowTitle("Remove a reservation")

        self.get_info()
        self.make_scroll_area()
        self.cancel()

        self.showMaximized()

    def get_info(self):
        font = QFont()
        font.setPointSize(25)

        space = QSpacerItem(0, 25)
        space2 = QSpacerItem(0, 25)


        info_layout = QVBoxLayout()
        phone_label = QLabel("Input guests phone number and press confirm:")
        phone_label.setFont(font)
        phone_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label = QLabel("")
        self.info_label.setFont(font)
        self.phone_input = QLineEdit()

        confirm = QPushButton("Confirm")
        confirm.setFont(font)

        info_layout.addWidget(phone_label)
        info_layout.addWidget(self.phone_input)
        info_layout.addWidget(confirm)
        info_layout.addItem(space)
        info_layout.addWidget(self.info_label)
        info_layout.addItem(space2)

        info_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        confirm.clicked.connect(self.confirmed_nr)

        self.main_layout.addLayout(info_layout)

    def make_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)

    def confirmed_nr(self):
        phone_nr = self.phone_input.text()
        if phone_nr in self.hotel.hotel_guests:
            self.info_label.setText("Please choose the reservations you wish to remove and press cancel reservation:")
            self.cancel_button.setText("Cancel reservation")
            self.choose_area(phone_nr)
        else:
            self.info_label.setText("Guest not found")
            self.cancel_button.setText("")
            self.empty_area()

    def choose_area(self, phone_nr):
        self.label_list = []
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        left_container = QVBoxLayout()
        right_container = QVBoxLayout()
        container_layout.addLayout(left_container)
        container_layout.addLayout(right_container)
        container_widget.setLayout(container_layout)

        font = QFont()
        font.setPointSize(20)

        for number in self.hotel.hotel_guests:
            if phone_nr == number:
                self.guest = self.hotel.hotel_guests[phone_nr]

        for reservation in self.guest.guest_reservations:
            start_date = reservation.start_date
            end_date = reservation.end_date
            room_type = reservation.room_type
            self.label_list.append(QCheckBox(room_type + ",    Check-in: " + str(start_date) + ",    Check-out: " + str(end_date)))

        for i in range(len(self.label_list)):
            label = self.label_list[i]
            label.setFont(font)
            if i % 2 == 0:
                left_container.addWidget(label)
                left_container.setAlignment(Qt.AlignmentFlag.AlignTop)
                left_container.addSpacing(10)
            else:
                right_container.addWidget(label)
                right_container.setAlignment(Qt.AlignmentFlag.AlignTop)
                right_container.addSpacing(10)

        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidget(container_widget)

    def empty_area(self):
        container_widget = QWidget()
        self.scroll_area.setWidget(container_widget)

    def cancel(self):
        font = QFont()
        font.setPointSize(25)
        self.cancel_button = QPushButton("")
        self.cancel_button.setFont(font)
        self.main_layout.addWidget(self.cancel_button)
        self.cancel_button.clicked.connect(self.cancel_confirmed)

    def cancel_confirmed(self):
        if self.info_label.text() != "Guest not found" and self.info_label.text() != "":
            for label in self.label_list:
                if label.isChecked():
                    text = label.text()
                    split_text = text.split(",")
                    room_type = split_text[0]
                    check_in = split_text[1][14:]
                    check_out = split_text[2][15:]
                    check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
                    check_out = datetime.strptime(check_out, '%Y-%m-%d').date()
                    self.hotel.remove_reservation(self.guest, check_in, check_out, room_type)
            self.cancel_successful()

    def cancel_successful(self):
        self.close()

        font = QFont()
        font.setPointSize(25)

        self.label = QLabel("Reservation canceled!")
        self.label.setFont(font)
        self.center(self.label)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label.show()

    def center(self, label):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        label.setGeometry(0, 0, 500, 500)
        x = (screen_geometry.width() - label.width()) // 2
        y = (screen_geometry.height() - label.height()) // 2
        label.move(x, y)