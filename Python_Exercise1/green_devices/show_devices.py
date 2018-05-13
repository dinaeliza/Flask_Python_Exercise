from flask import Blueprint, render_template

show_devices_bp = Blueprint('show_devices', __name__, template_folder='templates')

@show_devices_bp.route('/devices')
def view_devices():
    """List the devices with its name, value and notes."""
    return render_template('devices/device_list.html')

#@bp.route('/buy')
#def shop_devices():
#   """Shop for the devices."""
#    pass  '''
