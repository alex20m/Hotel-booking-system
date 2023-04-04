import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from datetime import date
from hotel import Hotel
from gui import GUI

"""
Main function of the program is used to start the GUI, while all of the GUI functions are implemented in the GUI class.
"""


def main():

    # Create a new PyQt6 application object
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())


main()
