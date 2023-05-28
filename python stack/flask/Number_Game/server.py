from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        response = ""
        session['number']=random.randint(1,100)
        print(session['number'])
    if request.method == "POST":
        clientnum = request.form['integer']
        if session['number'] > int(clientnum):
            print(session['number'])
            response = "Too low!"
        elif session['number'] < int(clientnum):
            response = "Too high!"
        else:
            response = "Correct answer!!"
    else:
        if "number" not in session:
            session["number"] = 1
    return render_template("index.html", response=response)











if __name__=="__main__":  
    app.run(debug=True)

