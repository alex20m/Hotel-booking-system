import unittest
from datetime import date, datetime
from reservations import Reservations
from hotel import Hotel


class TestReservations(unittest.TestCase):

    def test_reservation_not_through(self):
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, False)

    def test_reservation_through(self):
        start_date = date(2023, 3, 15)
        end_date = date(2023, 3, 20)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_through_same_day_in(self):
        start_date = date(2023, 3, 15)
        end_date = date(2023, 3, 23)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

    def test_reservation_through_same_day_out(self):
        start_date = date(2023, 3, 26)
        end_date = date(2023, 3, 30)
        room_type = "Cheap room"
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.check_availability(start_date, end_date, room_type)
        self.assertEqual(retval, True)

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
        hotel = Hotel("hotel_reservations_test")
        retval = hotel.read_previous_reservations("hotel_reservations_test")
        start_date = date(2023, 3, 23)
        end_date = date(2023, 3, 26)
        list = [["0442046661","Alex Mecklin","alex.mecklin@hotmail.com","Cheap room",start_date,end_date,"comments"]]
        self.assertEqual(retval, list)

    def test_write_to_file(self):
        pass

    def test_printing_interval(self):
        hotel = Hotel("hotel_reservations_test")
        start_date = date(2023, 3, 20)
        end_date = date(2023, 3, 25)
        retval = hotel.print_reservations_in_interval(start_date, end_date)
        self.assertEqual(retval, "0442046661, Alex Mecklin, alex.mecklin@hotmail.com, Cheap room, 2023-03-23, 2023-03-26, comments\n")
