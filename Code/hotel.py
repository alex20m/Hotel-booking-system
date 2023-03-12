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

    hotel_reservations is a list with all the hotels reservations. The elements are lists where the first element is the
    guests phone number, and the second element is the name, the third element is email, fourth element room_type,
    fifth element start_date, sixth end_date and seventh comments.

    hotel_guests is a dictionary where the key is the guests phone number and the value are the guest object.
    """

    def __init__(self, filename):
        self.hotel_guests = {}
        self.filename = filename
        self.hotel_reservations = self.read_previous_reservations(filename)

    def read_previous_reservations(self, filename):
        try:
            hotel_reservations = []
            file = open(filename, "r")
            for line in file:
                line = line.rstrip()
                split = line.split(";")
                phone_nr = split[0]
                name = split[1]
                email = split[2]
                start_date = split[3]
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = split[4]
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                room_type = split[5]
                comments = split[6]

                if phone_nr not in self.hotel_guests:
                    self.hotel_guests[phone_nr] = Guest(name, phone_nr, email, self.filename)
                hotel_reservations.append([phone_nr, name, email, room_type, start_date, end_date, comments])
            file.close()
            return hotel_reservations
        except OSError:
            return False

    def check_availability(self, start_date, end_date, room_type):
        for reservation in self.hotel_reservations:
            if reservation[3] == room_type:
                if start_date >= reservation[5]:
                    pass
                elif end_date <= reservation[4]:
                    pass
                else:
                    return False
        return True

    def print_reservations_in_interval(self, start_date, end_date):
        list = []
        string = ""
        for reservation in self.hotel_reservations:
            check_in = reservation[4]
            check_out = reservation[5]
            if (start_date <= check_in < end_date) or (start_date < check_out <= end_date): #Then it is in the interval
                list.append(reservation)
        for element in list:
            element[4] = str(element[4])
            element[5] = str(element[5])
            string += ", ".join(element)
            string += "\n"
        return string

    """"
    Start and end date are dates, room type and comment are string. Returns True if reservation was successful, 
    otherwise False, example if the room is booked. 
    """
    def make_reservation(self, start_date, end_date, room_type, comments, name, phone_nr, email):
        if self.check_availability(start_date, end_date, room_type):
            if phone_nr not in self.hotel_guests:
                self.hotel_guests[phone_nr] = Guest(name, phone_nr, email, self.filename)
            self.hotel_guests[phone_nr].add_reservation(start_date, end_date, room_type, comments)
            self.hotel_reservations.append([phone_nr, name, email, room_type, start_date, end_date, comments])
            self.write_reservations_to_file(phone_nr, name, email, start_date, end_date, room_type, comments, self.filename)
            return True
        else:
            return False

    def write_reservations_to_file(self, phone_nr, name, email, start_date, end_date, room_type, comments, filename):
        file = open(filename, "a")
        string = "{};{};{};{};{};{};{}\n".format(phone_nr, name, email, start_date, end_date, room_type, comments)
        file.write(string)
        file.close()



