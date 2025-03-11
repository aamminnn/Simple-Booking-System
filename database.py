import sqlite3

queries = {
    "User": """
            CREATE TABLE IF NOT EXISTS user(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            ic_number TEXT, 
            booking_id INTEGER)
            """,

    "Booking": """
            CREATE TABLE IF NOT EXISTS booking(
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER,
            source TEXT, 
            destination TEXT,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
            )
            """,

    "Status": """
            CREATE TABLE IF NOT EXISTS status(
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            booking_id INTEGER,
            payment_status TEXT, 
            FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
            )
            """,
}

def connect_database(queries:dict):
    connection = sqlite3.connect('database.db')
    # cursor = connection.execute("CREATE TABLE IF NOT EXISTS person(user_id, name, ic_number, booking_id)")
    for key, value in queries.items():
        connection.execute(value)
    cursor = connection.cursor()
    return connection, cursor

# table = cursor.execute("SELECT name FROM sqlite_master")
# print(table.fetchall())

# cursor.execute(
#     """
#     INSERT INTO person(user_id, first_name, last_name, booking_id) VALUES
#     (1, 'Ahmad','Ali',001),
#     (2, 'Bob','Besar',002),
#     (3, 'Chan','Choi',003)
#     """
# )

# person = Person(4, 'Sample User','5604', 104)
# person.add(cursor, 'person')

# person = cursor.execute("SELECT * from person")
# print(person.fetchall())



# connection.commit()
# connection.close()

