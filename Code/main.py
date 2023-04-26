import sys
from PyQt6.QtWidgets import QApplication
from hotel import Hotel
from gui import GUI

"""
Main function of the program is used to start the GUI, while all of the GUI functions are implemented in the GUI classes.
"""


def main():

    filename = "hotel_reservations"
    hotel = Hotel(filename)

    # Create a new PyQt6 application object
    app = QApplication(sys.argv)
    gui = GUI(hotel)
    sys.exit(app.exec())


main()
