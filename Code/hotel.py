from guest import Guest
from datetime import date, datetime
from cheap_room import CheapRoom
from normal_room import NormalRoom
from expensive_room import ExpensiveRoom
from guest import Guest


class Hotel:

    """
    We use the guests phone numbers to identify the guests, since guests can have the same names, but
    they can't have the same phone number. A phone number is 10 digits and is a string.

    hotel_reservations is a dictionary with all the hotels reservations. The key is a guest object
    and the values are a list where the first element is the check in date, the second element is checkout date.

    hotel_guests is a dictionary where the key is the guests phone number and the value are the guest object.
    """

    def __init__(self):
        self.hotel_reservations = {}
        self.hotel_guests = {}

    def read_previous_reservations(self, file_name):
        try:
            file = open(file_name, "r")
            for line in file:
                line = line.rstrip()
                dic_split = line.split(":")
                phone_nr = dic_split[0]
                val_split = dic_split[1].split(";")
                name = val_split[0]
                email = val_split[1]
                start_date = val_split[2]
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = val_split[3]
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                room_type = val_split[4]
                comments = val_split[5]

                guest = Guest(name, phone_nr, email)
                if phone_nr not in self.hotel_guests:
                    self.hotel_guests[phone_nr] = guest
                self.hotel_reservations[guest] = [start_date, end_date]
            file.close()
            return True
        except OSError:
            return False

    def check_availability(self, start_date, end_date):
        pass

    def print_reservations_in_interval(self, start_date, end_date):
        pass