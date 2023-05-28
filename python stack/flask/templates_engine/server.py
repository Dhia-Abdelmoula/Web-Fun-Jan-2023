from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html")
@app.route('/play/<int:x>')
def index2(x):
    return render_template("index2.html",x=x)
@app.route('/play/<int:x>/<color>')
def index3(x,color):
    return render_template("index3.html",x=x,color=color)


if __name__=="__main__":
    app.run(debug=True)