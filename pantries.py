import json

from flask_restful import Resource, fields, abort, marshal_with, reqparse
from flask import Response

from pantry_dao import PantryDao, pantries
from db_manager.db_utils import sql_query, sql_edit_insert, sql_delete, sql_query2

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
        results = sql_query('''SELECT * FROM Pantries''')

        js = json.dumps( [dict(ix) for ix in results] )
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    def post(self):
        args = parser.parse_args()

        dao = PantryDao(latitude=args['latitude'], longitude=args['longitude'])

        pantry_id = id(dao)

        latitude = args['latitude']
        longitude = args['longitude']
        sql_edit_insert('''INSERT INTO Pantries (PantryID, Latitude, Longitude) VALUES (?, ?, ?)''', (pantry_id, latitude, longitude))
        
        
        return 201
