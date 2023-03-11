import unittest
from datetime import date
from reservations import Reservations
from hotel import Hotel


class TestReservations(unittest.TestCase):

    def test_reservation_not_through(self):
        pass

    def test_reservation_through(self):
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        room_type = "Cheap room"


    def test_reservation_length(self):
        start_date = date(2023, 3, 30)
        end_date = date(2023, 3, 31)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_reservation_length(), 1)


    def test_price(self):
        start_date = date(2023, 3, 31)
        end_date = date(2023, 4, 3)
        guest = "Alex"
        room_type = "Expensive room"
        comments = "Champagne bottle in room"
        reservation = Reservations(guest, start_date, end_date, room_type, comments)
        self.assertEqual(reservation.get_price(), 90)

    def test_read_from_file(self):
        hotel = Hotel()
        retval = hotel.read_previous_reservations("hotel_reservations")
        self.assertEqual(retval, True)

    def test_write_to_file(self):
        pass

