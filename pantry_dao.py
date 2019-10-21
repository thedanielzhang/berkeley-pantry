from flask_restful import Resource, fields, marshal_with

pantries = {}

class PantryDao(object):
    def __init__(self, pantry_id, latitude, longitude):
        self.pantry_id = pantry_id
        self.latitude = latitude
        self.longitude = longitude