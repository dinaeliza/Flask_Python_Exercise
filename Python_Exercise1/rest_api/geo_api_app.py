from flask import Blueprint
from flask_restful import Api
from Python_Exercise1.resources.geo_notes import Geo_Notes

#app = Flask(__name__)

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.add_resource(Geo_Notes, '/geo_Notes', '/geo_Notes/<string:device_name>')

#app.register_blueprint(api_bp)

