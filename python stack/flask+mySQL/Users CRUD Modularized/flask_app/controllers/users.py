from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.user import Users

@app.route("/")
def index():
    users = Users.get_all()
    return render_template('read.html', users=users)

@app.route("/user/new")
def display():
    return render_template('new.html')

@app.route('/user/create', methods = ["post"])
def create():
    users = Users.save(request.form)
    print(request.form)
    return redirect('/')

@app.route("/user/<int:user_id>")
def one_user(user_id):
    data = {
        'id':user_id
    } 
    users = Users.get_one(data)
    
    return render_template("one_user.html",user=users)

@app.route("/user/<int:user_id>/edit")
def edit(user_id):
    
    user_to_edit = Users.get_one({'id': user_id})
    return render_template('edit.html', user = user_to_edit)

@app.route("/user/<int:user_id>/update", methods=['post'])
def update_user(user_id):
    
    Users.update(request.form)
    print(request.form)
    return redirect("/")
# @app.route('/user/<int:user_id>/update', methods=['post'])
# def update(user_id):
@app.route("/user/<int:user_id>/delete",methods=['post'])
def remove(user_id):
    data= {
        'id': user_id
    }
    Users.delete(data)
    print(request.form)
    return redirect('/')
        