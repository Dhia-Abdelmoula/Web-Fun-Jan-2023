from flask import Flask, render_template, redirect, request
from users import Users
app = Flask(__name__)


@app.route("/")
def index():
    users = Users.get_all()
    return render_template('read.html', users=users)
@app.route("/user/new")
def display():
    return render_template('new.html')
    
@app.route('/user/create', methods=["post"])
def create():
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    Users.save(data)
    print(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
