from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

# Temporary student (for now)
current_student = "Bilal"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rooms")
def show_rooms():

    conn = sqlite3.connect("hostel.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()

    conn.close()

    return render_template("rooms.html", rooms=rooms)


@app.route("/select/<int:room_id>")
def select_room(room_id):

    conn = sqlite3.connect("hostel.db")
    cursor = conn.cursor()

    # Check if student already has room
    cursor.execute("SELECT * FROM rooms WHERE student=?", (current_student,))
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return "You already selected a room!"

    # Assign room
    cursor.execute("""
    UPDATE rooms
    SET status='Occupied', student=?
    WHERE id=?
    """, (current_student, room_id))

    conn.commit()
    conn.close()

    return redirect("/rooms")


if __name__ == "__main__":
    app.run(debug=True)