from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dur = db.Column(db.Integer)
    
    def __init__(self, name, dur):
        self.name = name
        self.dur = dur
