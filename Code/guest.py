from datetime import datetime
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

    """
    Reads previous reservations from the file and saves them in a guest specific list with all of the guests reservation
    """
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

    """
    Creates a new reservtion object and ads it to the guests reservation list.
    """
    def add_reservation(self, check_in, check_out, room_type, comments):
        reservation = Reservations(self, check_in, check_out, room_type, comments)
        self.guest_reservations.append(reservation)

    """
    Gets and prints reservation history of guest
    """
    def print_reservation_history(self):
        string = ""
        counter = 1
        list = []
        for reservation in self.get_previous_reservations():
            string += "{}:    ".format(counter)
            list.append(reservation.room_type)
            list.append("Check in: " + str(reservation.start_date))
            list.append("Check out: " + str(reservation.end_date))
            list.append("Comments: " + reservation.comments)
            string += ",    ".join(list)
            string += "\n"
            string += "\n"
            list = []
            counter += 1
        return string

    """
    Removes a reservation from the guests reservation list
    """
    def remove_reservation(self, reservation):
        container_list = []
        for guest_reservation in self.guest_reservations:
            if guest_reservation.room_type == reservation[3] and guest_reservation.start_date == reservation[4] and guest_reservation.end_date == reservation[5]:
                pass
            else:
                container_list.append(guest_reservation)
        self.guest_reservations = container_list

