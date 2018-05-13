from flask import Flask, render_template

#def create_app():
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/devices')
def devices():
    return render_template('devices/device_list.html')

