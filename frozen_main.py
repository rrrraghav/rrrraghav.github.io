from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_frozen import Freezer

app = Flask(__name__)
bootstrap = Bootstrap5(app)
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    freezer.freeze()