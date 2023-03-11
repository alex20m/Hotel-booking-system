from room_type import RoomType


class NormalRoom(RoomType):

    def __init__(self):
        room_name = "Normal room"
        price = 20 #Price per night
        super.__init__(room_name, price)