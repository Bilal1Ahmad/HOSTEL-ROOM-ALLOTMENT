import sqlite3

conn = sqlite3.connect("hostel.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms(
id INTEGER PRIMARY KEY AUTOINCREMENT,
room_number INTEGER,
floor INTEGER,
capacity INTEGER,
status TEXT,
student TEXT
)
""")

rooms = [
(101,1,2,"Available"),
(102,1,2,"Occupied"),
(201,2,3,"Available"),
(202,2,2,"Available")
]

cursor.executemany(
"INSERT INTO rooms (room_number,floor,capacity,status) VALUES (?,?,?,?)",
rooms
)

conn.commit()
conn.close()

print("Database updated successfully")