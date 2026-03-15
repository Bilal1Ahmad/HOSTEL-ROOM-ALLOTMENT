import sqlite3

conn = sqlite3.connect("hostel.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms(
id INTEGER PRIMARY KEY AUTOINCREMENT,
room_number INTEGER,
status TEXT
)
""")

cursor.execute("INSERT INTO rooms (room_number,status) VALUES (101,'Available')")
cursor.execute("INSERT INTO rooms (room_number,status) VALUES (102,'Occupied')")
cursor.execute("INSERT INTO rooms (room_number,status) VALUES (103,'Available')")
cursor.execute("INSERT INTO rooms (room_number,status) VALUES (104,'Available')")

conn.commit()
conn.close()

print("Database created successfully")