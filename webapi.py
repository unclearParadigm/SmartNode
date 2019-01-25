#!/usr/bin/env python3

from time import time

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file

import configuration
from dto.get_dto import GetDto
from dto.set_dto import SetDto
from dto.apiresponse_dto import ApiResponse

api = Flask(__name__)
hal = configuration.get_hal()

session = None


@api.route('/', methods=['GET'])
def _main():
    return send_file('nodeui.html')


@api.route('/api/node/time', methods=['GET'])
def _time():
    return jsonify({'timestamp': int(time())}), 200


@api.route('/api/node/version', methods=['GET'])
def _version():
    return jsonify({'version': configuration.get_version()}), 200


@api.route('/api/node/sesssion/', methods=['GET'])
def _session():
    return jsonify({'session': session.__dict__ if session is not None else None})


@api.route('/api/node/about', methods=['GET'])
def _about():
    return jsonify({
        "description": configuration.NODE_DESCRIPTION,
        "maintainer": [val.__dict__ for val in configuration.NODE_MAINTAINER],
        "location": configuration.NODE_LOCATION,
        "config": [{'actor': key, 'config': val.__dict__} for key, val in configuration.get_pinconfig().items()]
    }), 200


@api.route('/api/node/set', methods=['POST'])
def _set() -> object:
    request_body = request.get_json(silent=True, cache=False, force=False)
    set_request = SetDto.create(request_body)

    if set_request is None:
        return ApiResponse(False, False, 'Invalid request, Schema Validation failed', request_body).make_response()

    if set_request.mode not in hal.SUPPORTED_OUTPUT_MODES:
        return ApiResponse(True, False, 'Hardware does not support the specified mode', request_body).make_response()

    if not hal.set(set_request):
        return ApiResponse(True, False, 'Could not set', request_body).make_response()

    return ApiResponse(True, True, 'OK', request_body).make_response()


@api.route('/api/node/get/<string:mode>/<int:actor>', methods=['GET'])
def _get(mode: str, actor: int) -> object:
    if mode not in hal.SUPPORTED_INPUT_MODES:
        return ApiResponse(False, False, 'Requested mode is invalid', {'mode': mode, 'actor': actor}).make_response()

    get_request = GetDto(str(mode), int(actor))
    success, read_value = hal.get(get_request)

    if not success:
        return ApiResponse(True, False, 'Could not get value', get_request.__dict__).make_response()

    return ApiResponse(True, True, 'OK', get_request.__dict__, read_value).make_response()


if __name__ == '__main__':
    if configuration.DEBUGMODE:
        api.run(host=configuration.DEBUGHOST, port=configuration.DEBUGPORT, debug=configuration.DEBUGMODE)
