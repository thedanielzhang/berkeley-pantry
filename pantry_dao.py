from flask_restful import Resource, fields, marshal_with

pantries = {}

class PantryDao(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude