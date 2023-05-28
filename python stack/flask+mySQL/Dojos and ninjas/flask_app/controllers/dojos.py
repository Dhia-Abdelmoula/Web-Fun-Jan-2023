from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/create', methods = ["POST"])
def new_dojo():
    dojos = Dojo.save(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def Get_ninjas(dojo_id):
    data = {
        "id" : dojo_id
    }
    dojo = Dojo.Get_ninjas_dojo(data)
    print(dojo,"------------"*25)
    return render_template('ninjas_in_dojo.html',dojo = dojo )
