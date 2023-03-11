from datetime import date


class Guest:

    """"
    self.guest_reservations is a list where all of one guests reservations are stored. The elements are lists, where
    the first element is the check in date and the second element checkout date. The length of the list is the amount of
    times the guest has stayed at the hotel. If a reservation is removed, the reservation should also be
    removed from this list.
    """

    def __init__(self, name, phone_nr, email):
        self.name = name
        self.phone_nr = phone_nr
        self.email = email
        self.guest_reservations = []


    def get_name(self):
        return self.name


    def read_previous_guest_reservations(self):
        pass


    def get_previous_reservations(self):
        return self.guest_reservations


    """"
    Start and end date are dates, room type and comment are string. Returns True if reservation was successful, 
    otherwise false, example if the room is booked. 
    """
    def make_reservation(self, start_date, end_date, room_type, comment):
        return False


    """"
    Writes to the guest_reservations file if the reservation was successful. Returns true if successful
    otherwise false.
    
    We use phone numbers to identify the guests because guests can have the same names, but not the same phone number. 
    The guest file is one file that looks like:
    
    phone_nr1
    start_date, end_date, room_type
    start_date, end_date, room_type
    start_date, end_date, room_type
    
    phone_nr2
    start_date, end_date, room_type
    start_date, end_date, room_type
    """
    def write_file(self, start_date, end_date, room_type, comment):
        return False


    """
    Gets and prints reservation history of guest
    """
    def print_reservation_history(self):
        pass