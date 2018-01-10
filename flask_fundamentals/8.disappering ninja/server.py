from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
def ninja():
    imagename = 'tmnt.png'
    return render_template('ninja.html', imgname = imagename)

@app.route('/ninja/<color>', methods=['GET'])
def show_ninja(color):
    if color == 'blue':
        imagename = 'leonardo.jpg'
    elif color == 'red':
        imagename = 'raphael.jpg'
    elif color == 'purple':
        imagename = 'donatello.jpg'
    elif color == 'orange':
        imagename = 'michelangelo.jpg'
    else:
        imagename = 'notapril.jpg'
    return render_template('ninja.html', imgname = imagename)

app.run(debug=True)
