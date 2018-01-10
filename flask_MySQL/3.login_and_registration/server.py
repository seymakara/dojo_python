from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key = 'kastamonuBEN'

mysql = MySQLConnector(app,'registration')

@app.route('/')
def index():
    session['loggedin'] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    print "hellooo"
    print request.form['action']

    if request.form['action'] == 'signin':
        checkdata = "SELECT * FROM users"
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        
        for user in (mysql.query_db(checkdata)):
            if user['email'] == email and user['password'] == hashed_password:
                session['loggedin'] = True
                flash("Welcome {} {}!".format(user['first_name'], user['last_name']))
                return redirect('/success')

        flash('Incorrect email or password!', category='failsignin')
        return redirect('/')

    else:
        checkdata = "SELECT * FROM users"
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        checkdata = "SELECT * FROM users"
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        confirm = request.form['confirm']

        data = {
                'first_name': firstname,
                'last_name': lastname,
                'email': email,
                'password': hashed_password
                }
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        register = True
        if len(firstname) < 3:
            flash("First name must be at least 2 letters long", category='failregister')
            register = False

        elif firstname.isalpha() == False:
            flash('First name cannot contain numbers', category='failregister')
            register = False

        if len(lastname) < 3:
            flash("Last name must be at least 2 letters long", category='failregister')
            register = False
        elif lastname.isalpha() == False:
            flash('Last name cannot contain numbers', category='failregister')
            register = False

        for user in (mysql.query_db(checkdata)):
            if user['email'] == email:
                flash("Invalid email adress!", category='failregister')
                register = False
        if not EMAIL_REGEX.match(email):
            flash("Invalid email address!", category='failregister')
            register = False
        
        if len(password) < 8:
            flash("Password must be at least 8 characters long", category='failregister')
            register = False
        if password != confirm:
            flash("Passwords do not match, please enter again!", category='failregister')
            register = False
        
        if register:
            mysql.query_db(query, data)
            flash("Welcome to MY website {} {}!".format(firstname, lastname))
            return redirect('/success')
        else:
            return redirect('/')
            
@app.route('/success')
def success():

    return render_template("success.html")


app.run(debug=True)