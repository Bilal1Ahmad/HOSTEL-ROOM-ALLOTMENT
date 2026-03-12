from flask import Flask, render_template

app = Flask(__name__)

# Sample room data
rooms = [
    {"number": 101, "status": "Available"},
    {"number": 102, "status": "Occupied"},
    {"number": 103, "status": "Available"},
    {"number": 104, "status": "Available"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rooms")
def show_rooms():
    return render_template("rooms.html", rooms=rooms)

if __name__ == "__main__":
    app.run(debug=True)