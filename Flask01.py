from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hey there!</h1> Welcome to the Home Page!"

@app.route("/<name>")
def user(name):
    return f"<h1>Hey There, {name}!</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("denied"))

@app.route("/denied")
def denied():
    return "<h1>Hey! I'm Sorry but you're not authorized to do that!<h1>"

if __name__ == "__main__":
    app.run() 

