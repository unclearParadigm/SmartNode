from time import time

from flask import jsonify
from flask import Blueprint
from backend import configuration

infoapi = Blueprint('info_api', __name__)


@infoapi.route('/api/node/time', methods=['GET'])
def get_current_system_time():
    return jsonify({'timestamp': int(time())}), 200


@infoapi.route('/api/node/version', methods=['GET'])
def get_backend_version():
    return jsonify({'version': configuration.get_version()}), 200


@infoapi.route('/api/node/about', methods=['GET'])
def get_node_about_information():
    return jsonify({
        "description": configuration.NODE_DESCRIPTION,
        "maintainer": [val.__dict__ for val in configuration.NODE_MAINTAINER],
        "location": configuration.NODE_LOCATION,
    }), 200


@infoapi.route('/api/node/gpioconfig', methods=['GET'])
def get_gpio_configuration():
    return jsonify([pinconfig.__dict__ for pinconfig in configuration.get_pinconfig()]), 200
