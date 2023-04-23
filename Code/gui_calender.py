from PyQt6.QtCore import QRegularExpression, Qt, QDate, QRect
from PyQt6.QtGui import QFont, QTextCharFormat, QColor, QBrush, QPixmap, QPalette
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit, QComboBox, QSpacerItem, \
    QMainWindow
from PyQt6 import QtWidgets
from datetime import date, timedelta, datetime

from PyQt6.uic.properties import QtCore

from reservations import Reservations



class GUICalender(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.setWindowTitle("Make a reservation")

        self.hotel = hotel
        self.start_date = None
        self.end_date = None
        self.start_set = False
        self.end_set = False
        self.room_type = None
        self.today = datetime.today().date()
        self.price = None
        self.name = ""
        self.email = ""
        self.phone_nr = ""
        self.comments = ""

        self.standard_color = QColor(23, 23, 23)
        self.transparent_red = QColor(255, 0, 0, 128)
        self.transparent_green = QColor(0, 255, 0, 128)
        self.select_color = QColor(0, 140, 0, 128)

        space = QSpacerItem(0, 50)
        space2 = QSpacerItem(0, 50)

        self.main_widget = QWidget()

        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.container_widget = QWidget()
        self.container_layout = QVBoxLayout()
        self.info_layout = QVBoxLayout()
        self.name_layout = QHBoxLayout()
        self.phone_layout = QHBoxLayout()
        self.email_layout = QHBoxLayout()
        self.comments_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout_left = QVBoxLayout()
        self.bottom_layout_right = QVBoxLayout()

        self.container_widget.setLayout(self.container_layout)

        self.make_calendar()
        self.container_layout.addItem(space)

        self.make_window()
        self.container_layout.addLayout(self.info_layout)

        self.info_layout.addLayout(self.name_layout)
        self.info_layout.addLayout(self.phone_layout)
        self.info_layout.addLayout(self.email_layout)
        self.info_layout.addLayout(self.comments_layout)

        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.make_info()
        self.container_layout.addItem(space2)
        self.confirmation()

        self.showMaximized()

        self.room_box.currentIndexChanged.connect(self.dates_not_available)
        self.choose_date_range()
        self.get_input()

    def make_calendar(self):

        font = QFont()
        font.setPointSize(40)

        self.label = QLabel("Choose room type:")
        self.label.setFont(font)
        self.container_layout.addWidget(self.label)

        self.room_box = QComboBox()
        self.room_box.addItems(["Not selected", "Cheap room", "Normal room", "Expensive room"])
        menu_font = QFont()
        menu_font.setPointSize(16)
        self.room_box.setFont(menu_font)
        self.room_box.setMinimumSize(500, 50)
        self.container_layout.addWidget(self.room_box)
        space = QSpacerItem(0, 20)
        self.container_layout.addItem(space)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumSize(640, 480)
        self.calendar.setStyleSheet("QTableView::item:selected { background-color: %s; }" % self.select_color.name())
        self.calendar.setSelectedDate(self.today - timedelta(days=1))

        self.container_layout.addWidget(self.calendar)

        self.price_label = QLabel("")
        self.price_label.setFont(font)

        self.container_layout.addWidget(self.price_label)

    def make_window(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setWidget(self.container_widget)
        self.main_layout.addWidget(self.scroll_area)

    def paint_calendar(self, start_date, end_date, color):
        format = QTextCharFormat()
        format.setBackground(QColor(color))
        while start_date <= end_date:
            self.calendar.setDateTextFormat(start_date, format)
            start_date += timedelta(days=1)

    def choose_date_range(self):
        self.calendar.selectionChanged.connect(self.set_range)
        self.confirm_button.clicked.connect(self.confirm_clicked)

    def set_range(self):
        self.price_label.setText("")
        self.standard_confirm()

        if self.room_type != None and self.room_type != "Not selected":
            chosen_date = self.calendar.selectedDate().toPyDate()
            if chosen_date >= self.today:

                if self.start_set and self.end_set:
                    self.start_set = False
                    self.end_set = False
                    self.paint_calendar(self.start_date, self.end_date, self.standard_color)
                    self.dates_not_available()
                    self.start_date = None
                    self.end_date = None
                    self.label.setText("Select check-in date:")

                if not self.start_set:
                    self.start_date = chosen_date
                    self.start_set = True
                    self.label.setText("Select check-out date:")
                elif self.start_set and not self.end_set:
                    self.end_date = chosen_date
                    self.end_set = True

                    if self.end_date > self.start_date:
                        if self.hotel.check_availability(self.start_date, self.end_date, self.room_type):
                            self.paint_calendar(self.start_date, self.end_date, self.transparent_green)
                            self.label.setText("Check-in and check-out dates selected")
                        else:
                            self.label.setText("Room not available, select check-in date:")
                            self.start_set = False
                            self.end_set = False
                    else:
                        self.label.setText("Select check-in date:")
            else:
                self.label.setText("Not available, select check-in date:")
                if self.start_set and self.end_set:
                    self.paint_calendar(self.start_date, self.end_date, self.standard_color)
                self.start_set = False
                self.end_set = False

        if self.label.text() == "Check-in and check-out dates selected":
            self.price = Reservations.get_price(self, self.start_date, self.end_date, self.room_type)
            self.price_label.setText("Price of stay: {}€".format(self.price))
            self.update_confirm()

    def confirm_clicked(self):
        if self.label.text() == "Check-in and check-out dates selected":
            if self.name != "" and self.phone_nr != "" and self.email != "":
                self.hotel.make_reservation(self.start_date, self.end_date, self.room_type, self.comments, self.name,
                                            self.phone_nr, self.email)
                self.close()

                self.widget = QWidget()
                main_layout = QVBoxLayout()
                self.widget.setLayout(main_layout)

                font = QFont()
                font.setPointSize(30)

                thanks_label = QLabel("Reservation successful!")
                thanks_label.setFont(font)
                thanks_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                image = QLabel()
                pixmap = QPixmap("image2.png").scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
                image.setPixmap(pixmap)
                image.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.center(self.widget)

                main_layout.addWidget(thanks_label)
                main_layout.addWidget(image)

                self.widget.show()

    def dates_not_available(self):
        self.standard_settings()
        self.standard_confirm()

        if not self.start_set and not self.end_set:
            self.label.setText("Select check-in date:")
        elif self.start_set and not self.end_set:
            self.label.setText("Select check-out date:")
        elif self.start_set and self.end_set:
            self.label.setText("Select check-in date:")

        selected_option = self.room_box.currentText()
        self.room_type = selected_option

        if selected_option == "Not selected":
            self.label.setText("Choose room type:")

        for reservation in self.hotel.hotel_reservations:
            check_in = reservation[4]
            check_out = reservation[5]
            self.paint_calendar(check_in, check_out, self.standard_color)

        for reservation in self.hotel.hotel_reservations:
            room_type = reservation[3]
            check_in = reservation[4]
            check_out = reservation[5]
            if self.room_type == room_type:
                self.paint_calendar(check_in, check_out, self.transparent_red)

    def standard_settings(self):
        self.start_set = False
        self.end_set = False
        self.start_date = None
        self.end_date = None
        self.price_label.setText("")

        start_date = self.today
        end_date = date(2100, 1, 1)
        self.paint_calendar(start_date, end_date, self.standard_color)

    def make_info(self):

        font = QFont()
        font.setPointSize(26)

        name_label = QLabel("Enter your name:")
        self.name_layout.addWidget(name_label)
        self.name_input = QLineEdit()
        self.name_layout.addWidget(self.name_input)
        name_label.setFont(font)

        phone_label = QLabel("Enter your phone number:")
        self.phone_layout.addWidget(phone_label)
        self.phone_input = QLineEdit()
        self.phone_layout.addWidget(self.phone_input)
        phone_label.setFont(font)

        email_label = QLabel("Enter your email:")
        self.email_layout.addWidget(email_label)
        self.email_input = QLineEdit()
        self.email_layout.addWidget(self.email_input)
        email_label.setFont(font)

        comments_label = QLabel("Do you have any additional comments?")
        self.comments_layout.addWidget(comments_label)
        self.comments_input = QTextEdit()
        self.container_layout.addWidget(self.comments_input)
        comments_label.setFont(font)

    def confirmation(self):

        font = QFont()
        font.setPointSize(40)

        self.confirmation_label = QLabel("Please enter booking details")
        self.container_layout.addWidget(self.confirmation_label)
        self.confirmation_label.setFont(font)
        self.confirmation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font.setPointSize(26)

        self.room_label = QLabel("")
        self.room_label.setFont(font)
        self.start_label = QLabel("")
        self.start_label.setFont(font)
        self.end_label = QLabel("")
        self.end_label.setFont(font)
        self.price_label_2 = QLabel("")
        self.price_label_2.setFont(font)

        self.name_label = QLabel("")
        self.name_label.setFont(font)
        self.phone_label = QLabel("")
        self.phone_label.setFont(font)
        self.email_label = QLabel("")
        self.email_label.setFont(font)

        space = QSpacerItem(0, 20)

        self.container_layout.addItem(space)

        self.bottom_layout_left.addWidget(self.room_label)
        self.bottom_layout_left.addWidget(self.start_label)
        self.bottom_layout_left.addWidget(self.end_label)
        self.bottom_layout_left.addWidget(self.price_label_2)

        self.bottom_layout_right.addWidget(self.name_label)
        self.bottom_layout_right.addWidget(self.phone_label)
        self.bottom_layout_right.addWidget(self.email_label)

        self.bottom_layout.addLayout(self.bottom_layout_left)
        self.bottom_layout.addLayout(self.bottom_layout_right)
        self.container_layout.addLayout(self.bottom_layout)

        space = QSpacerItem(0, 50)

        self.container_layout.addItem(space)
        self.confirm_button = QPushButton("Reserve room")
        self.confirm_button.setFont(font)
        self.container_layout.addWidget(self.confirm_button)

    def update_confirm(self):
        self.confirmation_label.setText("Confirm reservation details")
        self.room_label.setText("Room type: " + str(self.room_type))
        self.start_label.setText("Check-in: " + str(self.start_date))
        self.end_label.setText("Check-out: " + str(self.end_date))
        self.price_label_2.setText("Price of stay {}€".format(self.price))

        self.name_label.setText("Name: " + self.name)
        self.phone_label.setText("Phone number: " + self.phone_nr)
        self.email_label.setText("Email: " + self.email)

    def standard_confirm(self):
        self.confirmation_label.setText("Please enter booking details")
        self.room_label.setText("")
        self.start_label.setText("")
        self.end_label.setText("")
        self.price_label_2.setText("")

    def get_input(self):
        self.name_input.textChanged.connect(self.name_input_changed)
        self.phone_input.textChanged.connect(self.phone_input_changed)
        self.email_input.textChanged.connect(self.email_input_changed)
        self.comments_input.textChanged.connect(self.comment_input_changed)

    def name_input_changed(self, text):
        self.name = text
        self.update_confirm()

    def phone_input_changed(self, text):
        self.phone_nr = text
        self.update_confirm()

    def email_input_changed(self, text):
        self.email = text
        self.update_confirm()

    def comment_input_changed(self):
        text = self.comments_input.toPlainText()
        self.comments = text

    def center(self, window):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window.setGeometry(0, 0, 640, 480)
        x = (screen_geometry.width() - window.width()) // 2
        y = (screen_geometry.height() - window.height()) // 2
        window.move(x, y)

