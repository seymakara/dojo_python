from flask import Flask, render_template, request, redirect,session, flash
app = Flask(__name__)
app.secret_key = 'cokgizli'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    error = False
    if len(name) < 1:
        flash("Name cannot be empty!")
        error = True
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(comment) < 1:
        flash("Comment cannot be empty!")
        error = True
    if len(comment) >120:
        flash("Comment cannot be more than 120 character")
        error = True
    if error:
        return redirect('/')
    else:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template("result.html", firstname = name, location = location, language = language, comment = comment)
    return redirect("/")
app.run(debug = True)