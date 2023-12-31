from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/")
def home():
    message = "Hello, from Flask!"
    return render_template("index.html", message=message)

@app.route("/<path:name>")
def page(name):
    return send_from_directory("templates", name)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port="80")