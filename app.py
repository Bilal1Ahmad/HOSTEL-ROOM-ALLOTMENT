from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)