from flask import Flask
from flask_restful import Api
from Python_Exercise1.resources.geo_notes import Geo_Notes
#from resources import geo_notes

app1 = Flask(__name__)

api = Api(app1)

api.add_resource(Geo_Notes, '/Geo_Notes', '/Geo_Notes/<string:device_name>')

#if __name__ == '__main__':
#    app.run(debug=True)
