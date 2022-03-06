from flask import render_template, flash

from core import app


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
