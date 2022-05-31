from flask import Flask
from flask_marshmallow import Marshmallow
from orm import Plant

app = Flask(__name__)
ma = Marshmallow(app)

class PlantSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Plant