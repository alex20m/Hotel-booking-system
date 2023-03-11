class Reservations:

    def __init__(self, guest, start_date, end_date, room_type, comments):
        self.guest = guest
        self.start_date = start_date
        self.end_date = end_date
        self.room_type = room_type
        self.comments = comments


    def get_reservation_length(self):
        pass

    def get_price(self):
        pass

    def write_file(self):
        pass
