from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('homepage.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')
app.run(debug=True)