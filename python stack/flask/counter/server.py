from flask import Flask, render_template, request, redirect, 
app = Flask(__name__)
@app.route('/')
def increment():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def reset():
    session.pop('counter', None)

if __name__ == '__main__':
    app.run(debug=True)
