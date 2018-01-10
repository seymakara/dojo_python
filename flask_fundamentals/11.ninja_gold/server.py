from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'zxcvbnm,iuygf'



@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "log" not in session:
        session["log"] = []
    if "logdate" not in session:
        session["logdate"]= []

    return render_template("index.html", gold = session['gold'], log = session['log'], logdate = session['logdate'])

@app.route('/process', methods =["GET", 'POST'])
def result():
    if request.form['action'] == "farm":
        pay = random.randint(10,21)
        session['gold'] += pay
        session['log'].append("{} from farm".format(int(pay)))
        session["logdate"].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    elif request.form['action'] == "cave":
        pay = random.randint(5,11)
        session['gold'] += pay
        session['log'].append("{} from cave".format(int(pay)))
        session["logdate"].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    elif request.form['action'] == "house":
        pay = random.randint(2,6)
        session['gold'] += pay
        session['log'].append("{} from house".format(int(pay)))
        session["logdate"].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    elif request.form['action'] == "casino":
        pay = random.randint(-50,51)
        session['gold'] += pay
        session['log'].append("{} from casino".format(int(pay)))
        session["logdate"].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    elif request.form['action'] == "reset":
        session['gold'] = 0
        session['log'] = []
        session['logdate'] = []

    return redirect('/')

    

app.run(debug=True)