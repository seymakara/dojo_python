from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key = 'SenUcYuzMilyarYediYuzElliMilyon'

mysql = MySQLConnector(app,'wall')

@app.route('/')
def index():
    if not 'loggedin' in session: 
        return render_template('index.html')
    else:
        return redirect ('/wall')

@app.route('/process', methods=['POST'])
def signin():
    #sign in logic
    if request.form['action'] == 'signin':
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        checkdata = "SELECT * FROM users"
        for user in (mysql.query_db(checkdata)):
            if user['email'] == email and user['password'] == hashed_password:
                session['loggedin'] = True
                session['user_id'] = user['id']
                flash("Welcome {} {}!".format(user['first_name'], user['last_name']))
                return redirect('/wall')

        flash('Incorrect email or password!', category='failsignin')
        return redirect('/')

    #register logic
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        confirm = request.form['confirm']

        #set all data in a dictionary
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

        checkdata = "SELECT * FROM users"
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
            return redirect('/wall')
        else:
            return redirect('/')

@app.route('/process_message', methods = ['POST'] )
def process_message():
    data = {
            'message': request.form['message'],
            'user_id': session['user_id']
            }
    query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id) "
    mysql.query_db(query, data)
    return redirect ('/wall')

@app.route('/process_comment', methods = ['POST'] )
def process_comment():
    data = {
            'comment': request.form['comment'],
            'message_id': request.form['action'],
            'user_id': session['user_id']
            }
    query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id) "
    mysql.query_db(query, data)

    return redirect ('/wall')

@app.route('/wall')
def show():
    if not 'loggedin' in session: 
        flash("Please sign in!")
        return redirect('/')
    else:
        query_messages = "SELECT users.first_name, users.last_name, messages.message, messages.id, messages.created_at FROM users JOIN messages ON messages.user_id = users.id"
        messages = mysql.query_db(query_messages)

        query_comments = "SELECT users.first_name, users.last_name, messages.id, comments.comment, comments.message_id, comments.created_at FROM comments JOIN messages ON messages.id = comments.message_id JOIN users ON users.id = comments.user_id"
        comments = mysql.query_db(query_comments)
        print comments
        return render_template('wall.html', all_messages=messages, all_comments = comments)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)