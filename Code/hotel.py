

class Hotel:

    """
    We use the guests phone numbers to identify the guests, since guests can have the same names, but
    they can't have the same phone number.

    hotel_reservations is a dictionary with all the hotels reservations. The key is the guests phone number
    and the values are a list where the first element is the guests name, the second is element is
    check in date, the third element is checkout date, fourth element is room type and
    fifth element is comments made by guest when booking.

    guest_list is a dictionary where the key is the guests phone number, the values are lists, where
    the first element is the guests name, the second is the guests email address.
    """

    def __init__(self):
        self.hotel_reservations = {} #list with all of the hotels reservations
        self.guest_list = [] #list with all of the quests that have stayed at the hotel