import sqlite3
import os, json

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("SELECT name from sqlite_master")
table = cursor.fetchall()
# print(table)

cursor.execute("SELECT * from user")
user = cursor.fetchall()
print(user)

cursor.execute("SELECT * from booking")
user = cursor.fetchall()
print(user)

cursor.execute("SELECT * from status")
user = cursor.fetchall()
print(user)

# query = f"SELECT * FROM status WHERE booking_id = ?"
# cursor.execute(query, (91,))
# row = cursor.fetchone()
# print(row)

# query = f"INSERT INTO status (payment_id, booking_id, payment_status) VALUES (?, ?, ?)"
# cursor.execute(query, (11, 91, 12))
# row = cursor.fetchone()
# print(row)


if os.path.exists('id.json'):
    with open('id.json','r') as json_data:
        data = json.load(json_data)
        print(data)

user_id = data.get("user_id", 0)
booking_id = data.get("booking_id", 0)
payment_id = data.get("payment_id", 0)

user_id += 1
booking_id +=1
payment_id += 1

data["user_id"] = user_id
data["booking_id"] = booking_id
data["payment_id"] = payment_id


with open('id.json','w')as file:
    json.dump(data, file, indent=4)
