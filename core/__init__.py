from flask.config import Config
from flask import Flask

from config import Config
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object(Config)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mansur.ham44@gmail.com'
app.config['MAIL_PASSWORD'] = 'Xamerzaev95'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

from core  import routes