from model import *
from database import queries, connect_database
import os, json

print("Welcome to my booking system. Press 'q' to quit\n")
connection, cursor = connect_database(queries)
connection.commit()

options = ['Booking','Pay','Status']
booking_field = ['name','ic', 'source','destination','pay now? (yes / no)']
payment_status = None

if os.path.exists('id.json'):
    with open('id.json','r') as json_data:
        data = json.load(json_data)
        print(data)

user_id = data.get("user_id", 0)
booking_id = data.get("booking_id", 0)
payment_id = data.get("payment_id", 0)

while True:
    opt = input("Select Option (1.Booking / 2.Pay / 3.Status): ")
    if opt.lower() == 'q':
        connection.close()
        exit()
    if opt == '1':
        print('Make Your Booking!')
        user = {}
        for f in booking_field:
            value = input(f"Enter {f}: ")
            if value.lower() == 'yes':
                payment_status = 'yes'
            elif value.lower() == 'no':
                payment_status = 'no'
            user[f] = value

        # initialize
        name = user['name']
        ic = user['ic']
        source = user['source']
        destination = user['destination']
        user_id += 1
        booking_id +=1
        payment_id += 1

        # Add to db
        user = User(user_id, name, ic, booking_id)
        booking = Booking(booking_id, user_id, source, destination)
        status = Status(payment_id, booking_id, payment_status)

        user.add(cursor, 'user')
        booking.add(cursor, 'booking')
        status.add(cursor, 'status')
        connection.commit()

        print(f"Thank you for booking! Here is your Booking ID: {booking_id}")
        data["user_id"] = user_id
        data["booking_id"] = booking_id
        data["payment_id"] = payment_id
        with open('id.json','w')as file:
            json.dump(data, file, indent=4)

    if opt == '2':
        status = Status(payment_id, booking_id, payment_status)
        status_booking_id = input("Please enter booking id: ")
        check = status.check_payment_status(cursor, 'status',status_booking_id)
        print("Your payment ID: ", check[0])
        if check[2] == 'no':
            pay = input("Please pay any amount: ")
            print("Thank you for your payment")
        elif check[2] == 'yes':
            print('You have paid')

    if opt == '3':
        status = Status(payment_id, booking_id, payment_status)
        status_booking_id = input("Please enter booking id: ")
        check = status.check_payment_status(cursor, 'status',status_booking_id)
        print("Your payment ID: ", check[0])
        if check[2] == 'no':
            print("You have not paid")
        elif check[2] == 'yes':
            print("You have paid")

    print("\n")


    