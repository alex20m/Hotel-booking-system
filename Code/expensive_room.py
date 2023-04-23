from room_type import RoomType


class ExpensiveRoom(RoomType):

    def __init__(self):
        room_name = "Expensive room"
        price = 100 #Price per night
        super().__init__(room_name, price)