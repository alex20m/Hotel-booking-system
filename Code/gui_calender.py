from PyQt6.QtCore import QRegularExpression, Qt, QDate
from PyQt6.QtGui import QFont, QTextCharFormat, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit, QComboBox
from PyQt6 import QtWidgets
from hotel import Hotel
from datetime import date, timedelta, datetime
from guest import Guest



class GUICalender(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.start_date = None
        self.end_date = None
        self.start_set = False
        self.end_set = False
        self.room_type = None
        self.today = datetime.today().date()

        self.standard_color = QColor(23, 23, 23)
        self.transparent_red = QColor(255, 0, 0, 128)
        self.transparent_green = QColor(0, 255, 0, 128)

        self.main_widget = QWidget()

        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.container_widget = QWidget()
        self.container_layout = QVBoxLayout()
        self.container_widget.setLayout(self.container_layout)

        self.make_calendar()
        self.make_window()

        self.showMaximized()

        self.room_box.currentIndexChanged.connect(self.dates_not_available)
        self.choose_date_range()


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

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumSize(640, 480)
        self.container_layout.addWidget(self.calendar)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setFont(font)
        self.container_layout.addWidget(self.confirm_button)

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
                    if self.end_date >= self.start_date:
                        self.label.setText("Press confirm")
                    else:
                        self.label.setText("Select check-in date:")

                if self.start_set and self.end_set:
                    if self.hotel.check_availability(self.start_date, self.end_date, self.room_type):
                        self.paint_calendar(self.start_date, self.end_date, self.transparent_green)
                    else:
                        self.label.setText("Room not available, select check-in date:")

            else:
                self.label.setText("Not available, select check-in date:")
                if self.start_set and self.end_set:
                    self.paint_calendar(self.start_date, self.end_date, self.standard_color)


    def confirm_clicked(self):
        if self.start_set and self.end_set:
            if self.start_date <= self.end_date:
                if self.label.text() == "Press confirm":
                    print("Done")

    def dates_not_available(self):
        self.standard_settings()

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

        start_date = self.today
        end_date = date(2100, 1, 1)
        self.paint_calendar(start_date, end_date, self.standard_color)


