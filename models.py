from app import app
from flask_sqlalchemy import SQLAlchemy
from dbmanager import SQLAlchemyManager

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anaban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    power = db.Column(db.Integer)
    summary = db.Column(db.String(100))

    def __init__(self, dict):
        self.name = dict['name']
        self.power = dict['power']
        self.summary = dict['summary']

manager = SQLAlchemyManager(db=db, Table=Character)

