from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, \
    QScrollArea, QTextEdit, QToolBar, QLineEdit, QDateEdit, QSpacerItem
from PyQt6 import QtWidgets




class GUIPrint(QtWidgets.QMainWindow):

    def __init__(self, hotel, print_type):
        super().__init__()
        self.hotel = hotel
        self.guest = None
        self.phone_nr = None

        self.select_color = QColor(0, 140, 0, 128)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.toolbar = QToolBar()
        self.search_bar = QLineEdit()
        self.toolbar.addWidget(self.search_bar)

        font = QFont()
        font.setPointSize(40)
        self.not_found_label = QLabel("")
        self.not_found_label.setFont(font)
        self.not_found_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

    #Called when printing hotel reservations
    def print_hotel(self):
        self.make_calender()
        self.make_window("")

    #Called when printing guest reservations
    def print_guest(self):
        font = QFont()
        font.setPointSize(25)

        self.guest_layout = QVBoxLayout()

        self.guest_label = QLabel("Input guests phone number and press confirm:")
        self.guest_label.setFont(font)
        self.guest_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.phone_input = QLineEdit()
        self.phone_input.textChanged.connect(self.phone_input_changed)

        self.guest_confirm = QPushButton("Confirm")
        self.guest_confirm.setFont(font)

        self.guest_layout.addWidget(self.guest_label)
        self.guest_layout.addWidget(self.phone_input)
        self.guest_layout.addWidget(self.guest_confirm)

        self.guest_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addLayout(self.guest_layout)
        self.make_window("")

        self.guest_confirm.clicked.connect(self.confirmed_nr)

    #Makes the window with the scrollable area with a text thats the parameter
    def make_window(self, string):

        # We make a scrollable area if the text is long
        # The text should be read only
        # We also change the font so that is is big enough

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(string)
        self.scroll_area.setWidget(self.text_edit)
        self.text_edit.setReadOnly(True)
        font = QFont()
        font.setPointSize(18)
        self.text_edit.setFont(font)

        # We then make a toolbar with a search bar so the user can search for things instead of just scroll
        # Not working yet

        #self.addToolBar(self.toolbar)

        self.main_layout.addWidget(self.scroll_area)

    def phone_input_changed(self, text):
        self.phone_nr = text

    #Called when guest clicks on confirm
    def confirmed_nr(self):
        self.guest = None

        for phone_nr in self.hotel.hotel_guests:
            if phone_nr == self.phone_nr:
                self.guest = self.hotel.hotel_guests[phone_nr]

        if self.guest == None:
            string = "Guest has no reservations"
        else:
            self.not_found_label.setText("")
            string = self.guest.print_reservation_history()

        self.make_window(string)

    #Makes the small calender and info about what to input
    def make_calender(self):
        self.start_date = None
        self.end_date = None

        font = QFont()
        font.setPointSize(25)
        space = QSpacerItem(0, 50)

        label = QLabel("Choose interval to print reservations from and press confirm:")
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(label)
        self.main_layout.addItem(space)

        date_layout = QHBoxLayout()
        start_layout = QVBoxLayout()
        end_layout = QVBoxLayout()
        date_layout.addLayout(start_layout)
        date_layout.addLayout(end_layout)

        font.setPointSize(16)
        start_label = QLabel("Select start of interval:")
        end_label = QLabel("Select end of interval:")
        start_label.setFont(font)
        end_label.setFont(font)

        self.date_start = QDateEdit()
        self.date_start.setCalendarPopup(True)
        self.date_start.setDate(QDate.currentDate())
        self.start_date = self.date_start.date()

        self.date_end = QDateEdit()
        self.date_end.setCalendarPopup(True)
        self.date_end.setDate(QDate.currentDate())
        self.end_date = self.date_end.date()


        start_layout.addWidget(start_label)
        start_layout.addWidget(self.date_start)
        end_layout.addWidget(end_label)
        end_layout.addWidget(self.date_end)

        self.main_layout.addLayout(date_layout)

        confirm = QPushButton("Confirm")
        confirm.setFont(font)
        self.main_layout.addWidget(confirm)

        self.date_start.dateChanged.connect(self.start_changed)
        self.date_end.dateChanged.connect(self.end_changed)
        confirm.clicked.connect(self.confirmed_interval)

    def start_changed(self):
        selected_date = self.date_start.date()
        self.start_date = selected_date

    def end_changed(self):
        selected_date = self.date_end.date()
        self.end_date = selected_date

    #Gets all of the reservations in the chosen interval
    def confirmed_interval(self):
        string = ""
        if self.start_date != None and self.end_date != None:
            string = self.hotel.print_reservations_in_interval(self.start_date, self.end_date)
            if string == "":
                string = "No reservations in interval"

        self.make_window(string)








