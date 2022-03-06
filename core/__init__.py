from flask.config import Config
from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from core  import routes