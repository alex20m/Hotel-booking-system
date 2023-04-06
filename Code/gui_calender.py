from PyQt6.QtCore import QRegularExpression, Qt, QDate
from PyQt6.QtGui import QFont, QTextCharFormat, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit
from PyQt6 import QtWidgets
from hotel import Hotel
from datetime import date, timedelta
from guest import Guest



class GUICalender(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.start_date = None
        self.end_date = None
        self.start_set = False
        self.end_set = False

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
        self.choose_date_range()


    def make_calendar(self):

        self.label = QLabel("Select check-in date::")

        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.container_layout.addWidget(self.label)
        self.label.setMinimumSize(500, 100)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumSize(640, 480)
        self.container_layout.addWidget(self.calendar)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setFont(font)
        self.container_layout.addWidget(self.confirm_button)


        transparent_red = QColor(255, 0, 0, 128)
        self.paint_calendar(date(2023, 3, 10), date(2023, 3, 15), transparent_red)


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
        chosen_date = self.calendar.selectedDate().toPyDate()

        if self.start_set and self.end_set:
            self.start_set = False
            self.end_set = False
            self.calendar.setStyleSheet("background-color: None;")
            standard_color = QColor(23, 23, 23)
            self.paint_calendar(self.start_date, self.end_date, standard_color)
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
            transparent_green = QColor(0, 255, 0, 128)
            self.paint_calendar(self.start_date, self.end_date, transparent_green)

    def confirm_clicked(self):
        if self.start_set and self.end_set:
            if self.start_date <= self.end_date:
                print("Done")
