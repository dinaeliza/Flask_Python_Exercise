from flask import Flask

from green_devices import app
from rest_api.geo_api_app import app1
app.run()
app1.run()

