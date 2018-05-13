import functools
from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )

from werkzeug.exceptions import abort

#bp = Blueprint('show_devices', __name__)

#@bp.route('/')
def view_devices():
    """List the devices with its name, value and notes."""
    return render_template('devices/device_list.html')

#@bp.route('/buy')
def shop_devices():
    """Shop for the devices."""
    pass
