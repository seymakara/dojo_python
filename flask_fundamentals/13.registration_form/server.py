from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
app = Flask(__name__)
app.secret_key = 'erikdaligevrektir'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    email = request.form['e-mail']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    pwordconfirm = request.form['pwordconfirm']
    errorcount = 0

    if len(email) < 1:
        flash('Email cannot be empty!')
        errorcount+=1
    elif not EMAIL_REGEX.match(email):
        flash('Invalid e-mail address!')
        errorcount+=1

    if len(first_name) < 1 :
        flash('First name cannot be empty!')
        errorcount+=1
    elif first_name.isalpha() == False:
        flash('First name cannot contain numbers')
        errorcount+=1

    if len(last_name) < 1 :
        flash('Last cannot be empty!')
        errorcount+=1
    elif last_name.isalpha() == False:
        flash('Last name cannot contain numbers')
        errorcount+=1

    if len(password) < 1:
        flash('Password cannot be empty!')
        errorcount+=1
    elif len(password) < 8:
        flash('Passwords must be at least 8 characters long.')
        errorcount+=1
    elif not PASSWORD_REGEX.match(password):
        flash('Password must contain at least one uppercase letter, one lowercase letter and one number.')
        errorcount+=1

    if len(pwordconfirm) < 1 :
        flash('Password confirm cannot be empty!')
        errorcount+=1
    elif len(pwordconfirm) < 8:
        flash('Passwords must be atleast 8 characters long.')
        errorcount+=1

    if password != pwordconfirm:
        flash('Passwords do not match, please enter again!')
        errorcount+=1
        
    if errorcount == 0:
        flash('Your registration is successful!')

    return redirect('/')

app.run(debug=True)