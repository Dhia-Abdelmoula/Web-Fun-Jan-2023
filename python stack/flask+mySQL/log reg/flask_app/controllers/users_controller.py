from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# LOGIN PAGE
@app.route('/logreg')
def show_form():
    
    return render_template('register_login.html')

# REGISTER method
@app.route("/users/create", methods=['POST'])
def user_create():
    
    if not User.validate(request.form):
        return redirect ('/logreg')
    # HASH THE PASSWORD
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : pw_hash
    }
    # Create a user
    user_id = User.create(data)
    # Store user id in session
    session["user_id"] = user_id
    return redirect("/dashboard")
    # LOGIN
@app.route("/users/login", methods = ["POST"])
def login():
    
    data = {
        "email" : request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalide credentials ", "log")
        return redirect ('/logreg')

    # check password
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalide credentials","log")
        return redirect('/logreg')
    
    # ALL GOOD up to here
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dash():
    
    # route guard
    if 'user_id' not in session:
        return redirect('/logreg')
    
    data = {
        "id" : session['user_id']
    }
    
    user = User.get_by_id(data)
    return render_template('dashboard.html', user = user)
    # logout 
@app.route('/logout')
def logout():
        
    session.clear()
    return redirect('/logreg')