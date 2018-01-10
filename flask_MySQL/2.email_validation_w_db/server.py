from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key = 'jamiryo'

mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails) # pass data to our template

@app.route('/form', methods=['POST'])
def create():
    query = "INSERT INTO emails (email, created_at, updates_at) VALUES (:email, NOW(), NOW())"
    data = {
             'email': request.form['email'],
           }
    mysql.query_db(query, data)

    session['email'] = request.form['email']
    errorcount = 0
    if len(request.form['email']) < 1:
        flash('Email cannot be empty!')
        errorcount +=1
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email is  not valid')
        errorcount +=1'z
        return redirect('/')
    if errorcount == 0:
        flash('The email address you entered is a valid email address. Thank you!')
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

@app.route('/delete')
def deleteAll():
    query = "DELETE FROM emails WHERE id > 0 "
    mysql.query_db(query)
    return render_template('index.html')


app.run(debug=True)