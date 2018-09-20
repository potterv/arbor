from flask import Flask
#from arbor.app import views
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from arbor.app.views import views
from arbor.app.models import dbModel