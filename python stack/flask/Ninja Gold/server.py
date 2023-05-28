from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/process-money", methods=["POST"])
def process():
    if request.form["location"] == "farm":
        session["farmgold"] = int(random.randint(10, 20))
        session["tot_gold"] += session["farmgold"]
        print(session["farmgold"])
    if request.form["location"] == "cave":
        session["cavegold"] = int(random.randint(5, 10))
        print(session["farmgold"])
    if request.form["location"] == "house":
        session["housegold"] = int(random.randint(2, 5))
        print(session["farmgold"])
    if request.form["location"] == "casino":
        session["casinogold"] = int(random.randint(-50, 50))
        print(session["farmgold"])
    return redirect("/")


if __name__ == "__main__":
    app.run()
