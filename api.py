import sqlite3

from flask import Flask, g
from flask_restful import Resource, Api

from pantry import Pantry
from pantries import Pantries

app = Flask(__name__)
api = Api(app)

DATABASE = 'db_manager/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Init from python shell
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('db_manager/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/test')
api.add_resource(Pantry, '/pantry/<string:pantry_id>')
api.add_resource(Pantries, '/pantry')

if __name__ == '__main__':
    app.run(debug=True)