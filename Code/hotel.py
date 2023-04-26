from datetime import date, datetime
from guest import Guest


class Hotel:

    """
    We use the guests phone numbers to identify the guests, since guests can have the same names, but
    they can't have the same phone number. A phone number is 10 digits and is a string.

    hotel_reservations is a list with all the hotels reservations. The elements are lists where the first element is the
    guests phone number, and the second element is the name, the third element is email, fourth element room_type,
    fifth element start_date, sixth end_date and seventh comments.

    hotel_guests is a dictionary where the key is the guests phone number and the value are the guest object.
    If a guest has removed all of their reservations, the guest is also removed from this list.
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
                if start_date > reservation[5]:
                    pass
                elif end_date < reservation[4]:
                    pass
                else:
                    return False
        return True

    def print_reservations_in_interval(self, start_date, end_date):
        list = []
        counter = 1
        string = ""
        for reservation in self.hotel_reservations:
            check_in = reservation[4]
            check_out = reservation[5]
            if (start_date <= check_in <= end_date) or (start_date <= check_out <= end_date): #Then it is in the interval
                list.append(reservation)
        for element in list:
            string += "{}:    ".format(counter)
            string += "Phone nr: "
            string += element[0]
            string += ",    Name: "
            string += element[1]
            string += ",    Email: "
            string += element[2]
            string += ",    Room type: "
            string += element[3]
            string += ",    Check-in: "
            string += str(element[4])
            string += ",    Check-out: "
            string += str(element[5])
            string += ",    Comments: "
            string += element[6]
            string += "\n"
            string += "\n"
            counter += 1
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

        with open(filename, "a") as file:
            string = "{};{};{};{};{};{};{}\n".format(phone_nr, name, email, start_date, end_date, room_type, comments)
            file.write(string)

    def get_guest_reservations(self, phone_nr):
        if phone_nr in self.hotel_guests:
            return self.hotel_guests[phone_nr].get_previous_reservations()
        else:
            return False

    def remove_reservation(self, guest, remove_start, remove_end, remove_room):
        string = ""
        container_list = []
        container_dic = {}
        with open(self.filename, "w") as file:
            for hotel_reservation in self.hotel_reservations:
                phone_nr = hotel_reservation[0]
                name = hotel_reservation[1]
                email = hotel_reservation[2]
                room_type = hotel_reservation[3]
                start_date = hotel_reservation[4]
                end_date = hotel_reservation[5]
                comments = hotel_reservation[6]

                if phone_nr == guest.phone_nr and room_type == remove_room and start_date == remove_start and end_date == remove_end:
                    guest.remove_reservation(hotel_reservation)
                else:
                    string += "{};{};{};{};{};{};{}\n".format(phone_nr, name, email, start_date, end_date, room_type, comments)
                    container_list.append(hotel_reservation)

            file.write(string)
            self.hotel_reservations = container_list

            if len(guest.guest_reservations) == 0:
                for person in self.hotel_guests:
                    if guest.phone_nr == person:
                        pass
                    else:
                        container_dic[person] = self.hotel_guests[person]
                self.hotel_guests = container_dic





