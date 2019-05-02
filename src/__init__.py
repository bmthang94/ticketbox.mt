from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT']
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "database.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

from src.models.user import User
from src.models.event import Event 
from src.models.ticket import Ticket 
from src.models.ticket_type import Ticket_Types 
from src.models.images import Image
from src.models.orders import Orders 
from src.models.venue import Venue 
from src.models.organizer import Organizer
from src.models.categories import Category

migrate = Migrate(app, db)
from src.components.events.views import events_blueprint
app.register_blueprint(events_blueprint, url_prefix="/events")