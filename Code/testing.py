import unittest
from datetime import date
from reservations import Reservations
from hotel import Hotel
from guest import Guest


class TestReservations(unittest.TestCase):

    def test_reservation_not_through(self):
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, False)

    def test_reservation_through(self):
        start_date = date(2023, 4, 15)
        end_date = date(2023, 4, 20)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_same_day_in(self):
        start_date = date(2023, 3, 15)
        end_date = date(2023, 3, 23)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, False)

    def test_reservation_same_day_out(self):
        start_date = date(2023, 3, 26)
        end_date = date(2023, 3, 30)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, False)

    def test_reservation_length(self):
        start_date = date(2023, 3, 30)
        end_date = date(2023, 3, 31)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_reservation_length(), 1)

    def test_remove(self):
        hotel = Hotel("hotel_reservations")
        guest = Guest("Alex", "112", "email", "hotel_reservations_test")
        start_date = date(2023, 4, 22)
        end_date = date(2023, 4, 29)
        room_type = "Expensive room"
        hotel.remove_reservation(guest, start_date, end_date, room_type)

    def test_price(self):
        start_date = date(2023, 3, 31)
        end_date = date(2023, 4, 3)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_price(start_date, end_date, room_type), 300)

    def test_read_from_file(self):
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.read_previous_reservations("hotel_reservations_test")
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        start_date2 = date(2023, 3, 10)
        end_date2 = date(2023, 3, 15)
        list = [["0442046661","Alex Mecklin","alex.mecklin@hotmail.com","Cheap room",start_date,end_date,"-"], ["112", "Alex", "email@test.com", "Cheap room", start_date2, end_date2, "-"]]
        self.assertEqual(retval, list)

    def test_printing_interval(self):
        hotel = Hotel("hotel_reservations_test")
        start_date = date(2023, 3,12)
        end_date = date(2023, 3, 16)
        retval = hotel.print_reservations_in_interval(start_date, end_date)
        self.assertEqual(retval, "Phone nr: 112,    Name: Alex,    Email: email@test.com,    Room type: Cheap room,    Check-in: 2023-03-10,    Check-out: 2023-03-15,    Comments: -\n\n")

    """
    The function below needs to be run independently, otherwise it disrupts the other tests when it writes to the test text file.
    """

    """
    def test_make_reservation(self):
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        room_type = "Normal room"
        comments = "comments"
        name = "Alex Mecklin"
        email = "alex.mecklin@hotmail.com"
        phone_nr = "0442046661"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.make_reservation(start_date, end_date, room_type, comments, name, phone_nr, email)
        self.assertEqual(retval, True)
    """

    def test_print_guest_reservations(self):

        guest = Guest("Alex", "112", "alex.mecklin@hotmail.com", "hotel_reservations_test")
        retval = guest.print_reservation_history()
        str = "Cheap room,    Check in: 2023-03-10,    Check out: 2023-03-15,    Comments: -\n\n"
        self.assertEqual(retval, str)


