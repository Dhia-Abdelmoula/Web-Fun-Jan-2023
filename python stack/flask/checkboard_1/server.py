from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<col_one>')
@app.route('/<int:x>/<int:y>/<col_one>/<col_two>')
def checkboard(x=8, y=8, col_one='red',col_two='green'):
    return render_template('index.html', rows=x, columns=y, col_one=col_one,col_two=col_two)

if __name__ == '__main__':
    app.run(debug=True)