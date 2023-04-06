from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit
from PyQt6 import QtWidgets
from hotel import Hotel
from datetime import date
from guest import Guest



class GUIPrint(QtWidgets.QMainWindow):

    def __init__(self, hotel, print_type):
        super().__init__()
        self.hotel = hotel

        self.main_widget = QWidget()

        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        if print_type == "Hotel":
            self.setWindowTitle("Hotel reservations")
            self.print_hotel()
        elif print_type == "Guest":
            self.setWindowTitle("Guest reservations")
            self.print_guest()

        self.showMaximized()

    def print_hotel(self):
        start_date = date(2023, 3, 10)
        end_date = date(2023, 3, 26)
        string = self.hotel.print_reservations_in_interval(start_date, end_date)
        self.make_window(string)

    def print_guest(self):
        guest = Guest("Alex", "0442046661", "alex.mecklin@hotmail.com", "hotel_reservations")
        string = guest.print_reservation_history()
        self.make_window(string)

    def make_window(self, string):

        # We make a scrollable area if the text is long
        # The text should be read only
        # We also change the font so that is is big enough
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(string)
        scroll_area.setWidget(self.text_edit)
        self.text_edit.setReadOnly(True)
        font = QFont()
        font.setPointSize(22)
        self.text_edit.setFont(font)

        # We then make a toolbar with a search bar so the user can search for things instead of just scroll
        # Not working yet
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        self.search_bar = QLineEdit()
        toolbar.addWidget(self.search_bar)

        self.main_layout.addWidget(scroll_area)



