import sqlite3

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
    
    def execute_queries(self, query):
        if self.cursor:
            self.cursor.execute(query)
            self.connection.commit()
        else:
            raise Exception("Database connection not established!")


        

class User(Database):
    def __init__(self, user_id, name, ic_number, booking_id):
        self.user_id = user_id
        self.name = name
        self.ic_number = ic_number
        self.booking_id = booking_id

    def add(self, cursor, table):
        self.cursor = cursor
        query = f"INSERT INTO {table} (user_id, name, ic_number, booking_id) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (self.user_id, self.name, self.ic_number, self.booking_id))


class Booking(Database):
    def __init__(self, booking_id, user_id, source, destination):
        self.booking_id = booking_id
        self.user_id = user_id
        self.source = source
        self.destination = destination

    def add(self, cursor, table):
        self.cursor = cursor
        query = f"INSERT INTO {table} (booking_id, user_id, source, destination) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (self.booking_id, self.user_id, self.source, self.destination))

class Status(Database):
    def __init__(self, payment_id=None, booking_id=None, payment_status=None):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.payment_status = payment_status

    def add(self, cursor, table):
        self.cursor = cursor
        query = f"INSERT INTO {table} (payment_id, booking_id, payment_status) VALUES (?, ?, ?)"
        self.cursor.execute(query, (self.payment_id, self.booking_id, self.payment_status))

    def check_payment_status(self, cursor, table, booking_id):
        self.cursor = cursor
        query = f"SELECT * FROM {table} WHERE booking_id = ?"
        self.cursor.execute(query, (booking_id,))
        row = self.cursor.fetchone()
        return row
    
    def update_payment_status(self, cursor, booking_id, payment_status):
        self.cursor = cursor
        query = "UPDATE status SET payment_status = ? WHERE booking_id = ?"
        self.cursor.execute(query, (payment_status, booking_id))

