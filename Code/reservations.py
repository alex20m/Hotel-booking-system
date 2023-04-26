from cheap_room import CheapRoom
from normal_room import NormalRoom
from expensive_room import ExpensiveRoom


class Reservations:

    def __init__(self, guest, start_date, end_date, room_type, comments):
        self.guest = guest
        self.start_date = start_date
        self.end_date = end_date
        self.room_type = room_type
        self.comments = comments


    """
    Reservation length is in amount of nights. You have to book at least one night.
    """
    def get_reservation_length(self):
        return (self.end_date - self.start_date).days

    def get_price(self, start_date, end_date, room_type):

        if room_type == "Cheap room":
            cheap_room = CheapRoom()
            price = cheap_room.get_price()

        elif room_type == "Normal room":
            normal_room = NormalRoom()
            price = normal_room.get_price()

        elif room_type == "Expensive room":
            expensive_room = ExpensiveRoom()
            price = expensive_room.get_price()

        length = (end_date - start_date).days

        return price * length
