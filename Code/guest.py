from datetime import date, datetime
from reservations import Reservations

class Guest:

    """"
    self.guest_reservations is a list where all of one guests reservations are stored. The elements are reservation
    objects. The length of the list is the amount of times the guest has stayed at the hotel.
    If a reservation is removed, the reservation should also be removed from this list.
    """

    def __init__(self, name, phone_nr, email, filename):
        self.name = name
        self.phone_nr = phone_nr
        self.email = email
        self.guest_reservations = self.read_previous_guest_reservations(filename)

    def get_name(self):
        return self.name

    def read_previous_guest_reservations(self, filename):
        list = []
        file = open(filename, "r")
        for line in file:
            line = line.rstrip()
            split_list = line.split(";")
            if split_list[0] == self.phone_nr:
                start_date = datetime.strptime(split_list[3], '%Y-%m-%d').date()
                end_date = datetime.strptime(split_list[4], '%Y-%m-%d').date()
                reservation = Reservations(self, start_date, end_date, split_list[5], split_list[6])
                list.append(reservation)
        file.close()
        return list

    def get_previous_reservations(self):
        return self.guest_reservations

    def add_reservation(self, check_in, check_out, room_type, comments):
        reservation = Reservations(self, check_in, check_out, room_type, comments)
        self.guest_reservations.append(reservation)

    """
    Gets and prints reservation history of guest
    """
    def print_reservation_history(self):
        string = ""
        list = []
        for reservation in self.get_previous_reservations():
            list.append(reservation.room_type)
            list.append("Check in: " + str(reservation.start_date))
            list.append("Check out: " + str(reservation.end_date))
            list.append("Comments: " + reservation.comments)
            string += ", ".join(list)
            string += "\n"
            list = []
        return string