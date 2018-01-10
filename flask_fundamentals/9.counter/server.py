from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "soSecret"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/level1')
def level1():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return redirect('/')


app.run(debug=True)