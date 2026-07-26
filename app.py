from flask import Flask

app = Flask(__name__)

@app. route("/")
def home():
    return "Hello, World! My first Flask API!"

@app.route("/about")
def about():
    return "This is Adithyan's backend API"

if __name__ == "__main__":
    app.run(debug=True)