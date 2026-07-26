from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! My first Flask API!"

@app.route("/about")
def about():
    return "This is Adithyan's backend API"

@app.route("/users")
def get_users():
    users = [
        {"id": 1, "name": "Adithyan", "role": "developer"},
        {"id": 2, "name": "Rahul", "role": "designer"},
        {"id": 3, "name": "Priya", "role": "manager"}
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)