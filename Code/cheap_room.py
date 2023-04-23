from room_type import RoomType


class CheapRoom(RoomType):

    def __init__(self):
        room_name = "Cheap room"
        price = 50 #Price per night
        super().__init__(room_name, price)