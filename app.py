from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route("/")
def index():
    return send_from_directory("html","index.html")

@app.route("/<path:name>")
def page(name):
    return send_from_directory("html",name)

if __name__ == "__main__":
    app.run(debug=True)