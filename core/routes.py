from flask import render_template, flash

from core import app
from flask import request
from flask_mail import Message
from . import mail


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')    
        msg = Message("С вами хочет связаться новый клиент!",sender="mansur.ham44@gmail.com" ,recipients=['mansur.ham44@gmail.com'])
        msg.body = f"Мансур, красавчик, у тебя новый заказ. cвяжись мой босс с: {text}"
        mail.send(msg)
    return render_template('index.html')
