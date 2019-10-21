from flask_restful import Resource, fields, abort, marshal_with, reqparse
from pantry_dao import PantryDao, pantries 

parser = reqparse.RequestParser()
parser.add_argument('latitude', type=float, help='Latitude of pantry')
parser.add_argument('longitude', type=float, help='Longitude of pantry')

resource_fields = {
    'latitude': fields.Float,
    'longitude': fields.Float,
}

def validate_item_exists(pantry_id):
    if pantry_id not in pantries:
        abort(404, message="Pantry {} doesn't exist".format(pantry_id))

class Pantry(Resource):
    
    @marshal_with(resource_fields)
    def get(self, pantry_id):
        validate_item_exists(pantry_id)
        return pantries[pantry_id]

    def delete(self, pantry_id):
        validate_item_exists(pantry_id)
        del pantries[pantry_id]
        return '', 204

    @marshal_with(resource_fields)
    def put(self, pantry_id):
        args = parser.parse_args()
        dao = PantryDao(pantry_id=pantry_id, latitude=args['latitude'], longitude=args['longitude'])
        pantries[pantry_id] = dao
        return pantries[pantry_id], 201