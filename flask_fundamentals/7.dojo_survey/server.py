from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    if name is None or name == "":
        name = "Please update your name"
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", firstname = name, location = location, language = language, comment = comment)
    return redirect("/")
app.run(debug = True)