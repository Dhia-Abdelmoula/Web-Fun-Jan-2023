from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.ninja import Ninja

from flask_app.models.dojo import Dojo

@app.route("/ninjas/new")
def new_ninja():
    dojos = Dojo.get_all()
    

    return render_template('new_ninja.html', dojos=dojos)

@app.route("/ninjas/create", methods=["POST"])
def create_ninja():
    print(request.form,"*"*25)
    Ninja.save(request.form)
    return redirect('/')
