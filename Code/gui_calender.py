from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCalendarWidget, \
    QBoxLayout, QGraphicsRectItem, QScrollArea, QTextEdit, QSizePolicy, QToolBar, QLineEdit
from PyQt6 import QtWidgets
from hotel import Hotel
from datetime import date
from guest import Guest


class GUICalender(QtWidgets.QMainWindow):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.start_date = None
        self.end_date = None

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

    def make_calendar(self):

        label = QLabel("Select start date:")
        font = QFont()
        font.setPointSize(20)
        label.setFont(font)
        label.setMinimumSize(500, 50)
        self.container_layout.addWidget(label)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumSize(640, 480)
        self.container_layout.addWidget(self.calendar)

        self.calendar.selectionChanged.connect(self.print_selected_date)

    def make_window(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setWidget(self.container_widget)
        self.main_layout.addWidget(self.scroll_area)

    def print_selected_date(self):
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        print(selected_date)




