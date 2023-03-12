from datetime import date
from hotel import Hotel


def main():

    check_in = date(2023, 3, 9)
    check_out = date(2023, 3, 10)
    name = "Alex"
    email = "email@test.com"
    comment = "-"
    hotel = Hotel("hotel_reservations_test")
    room_type = "Cheap room"
    phone_nr = "112"
    print(hotel.get_guest_reservations("112")[0].get_price())

main()