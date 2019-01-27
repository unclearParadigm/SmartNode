#!/usr/bin/env python3

from flask import Flask
from backend import configuration

from backend.blueprints.infoapi import infoapi
from backend.blueprints.staticapi import staticapi
from backend.blueprints.getsetapi import getsetapi
from backend.blueprints.configapi import configapi

api = Flask(__name__)
api.register_blueprint(infoapi)
api.register_blueprint(staticapi)
api.register_blueprint(getsetapi)
api.register_blueprint(configapi)

if __name__ == '__main__':
    if configuration.DEBUGMODE:
        api.run(host=configuration.DEBUGHOST, port=configuration.DEBUGPORT, debug=configuration.DEBUGMODE)
