from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello , World !!!!!!!'

from green_devices.show_devices import show_devices_bp
app.register_blueprint(show_devices_bp)

from rest_api.geo_api_app import api_bp
app.register_blueprint(api_bp)

app.run()

