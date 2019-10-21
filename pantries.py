from flask_restful import Resource, fields, abort, marshal_with, reqparse
from flask import Response
from pantry_dao import PantryDao, pantries
import json

parser = reqparse.RequestParser()
parser.add_argument('latitude', type=float, help='Latitude of pantry')
parser.add_argument('longitude', type=float, help='Longitude of pantry')

resource_fields = {
    'latitude': fields.Float,
    'longitude': fields.Float,
}

def obj_to_dict(obj):
    return obj.__dict__

class Pantries(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        js = json.dumps(pantries, default=obj_to_dict)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        pantry_id = 0

        if (len(pantries.keys()) != 0):
            pantry_id = int(max(pantries.keys())) + 1
        
        dao = PantryDao(pantry_id=pantry_id, latitude=args['latitude'], longitude=args['longitude'])
        pantries[pantry_id] = dao
        return pantries[pantry_id]
