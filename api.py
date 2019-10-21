from flask import Flask
from flask_restful import Resource, Api
from pantry import Pantry
from pantries import Pantries

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/test')
api.add_resource(Pantry, '/pantry/<string:pantry_id>')
api.add_resource(Pantries, '/pantry')

if __name__ == '__main__':
    app.run(debug=True)