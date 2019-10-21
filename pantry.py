from flask_restful import Resource, fields, marshal_with
from pantry_dao import PantryDao  

pantries = {}

resource_fields = {
    'latitude': fields.Float,
    'longitude': fields.Float,
}


class Pantry(Resource):
    def get(self, pantry_id):
        # @marshal_with(resource_fields)
        return { pantry_id: pantries[pantry_id] }

    def put(self, pantry_id):
        pantries[pantry_id] = request.form['data']
        return { pantry_id: pantries[pantry_id] }