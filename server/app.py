from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_restful import Api, Resource
from flask_cors import CORS
import config
from serial import PlantSchema
from orm import Plant

# configuration
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# set app config
app.config['SQLALCHEMY_DATABASE_URI'] = config.conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)
# api = Api(app)

plant = Plant("melon",1)
plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)


@app.route('/plants', methods=['GET'])
def get_plants():
    plants =  Plant.query.with_entities(Plant.name, Plant.dur)
    # return jsonify(plants_schema.dump(plants))
    # return jsonify(f"{plants}")

    return jsonify(f"{plants}")


@app.route('/plants', methods=['POST'])
def add_plant():
    # id = request.json.get('id', '')
    name = request.json.get('name', '')
    dur = request.json.get('dur', '')
    plant = Plant(name=name, dur=dur)
    db.session.add(plant)
    db.session.commit()
    return jsonify(f"{plant}")

if __name__ == '__main__':
    app.run()
