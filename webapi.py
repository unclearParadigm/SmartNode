from time import time

from flask import Flask
from flask import request
from flask import jsonify

import configuration
from dto.get_dto import GetDto
from dto.set_dto import SetDto
from dto.apiresponse_dto import ApiResponse


hal = configuration.get_hal()
api = Flask(__name__)


@api.route('/api/node/time', methods=['GET'])
def _time():
    return jsonify({'timestamp': int(time())}), 200


@api.route('/api/node/version', methods=['GET'])
def _version():
    return jsonify({'version': configuration.get_version()}), 200


def _about():
    pass


@api.route('/api/node/set', methods=['POST'])
def _set() -> object:
    request_body = request.get_json(silent=True, cache=False, force=False)
    set_request = SetDto.create(request_body)

    if set_request is None:
        return ApiResponse(False, False, 'Invalid request, Schema Validation failed', request_body).make_response()

    if not hal.set(set_request):
        return ApiResponse(True, False, 'Could not set', set_request).make_response()

    return ApiResponse(True, True, 'OK', set_request).make_response()


@api.route('/api/node/get/<string:output>/<int:actor>', methods=['GET'])
def _get(output: str, actor: int) -> object:
    if output not in ['digital', 'analog', 'pwm']:
        apianswer = ApiResponse(False, False, 'Invalid request. Unknown output', {'output': output, 'actor': actor})
        return apianswer.make_response()

    get_request = GetDto(str(output), int(actor))
    success, read_value = hal.get(get_request)

    if not success:
        return ApiResponse(True, False, 'Could not get', get_request).make_response()

    return ApiResponse(True, True, 'OK', get_request, read_value).make_response()


if __name__ == '__main__':
    if configuration.DEBUGMODE:
        api.run(host=configuration.DEBUGHOST, port=configuration.DEBUGPORT, debug=configuration.DEBUGMODE)


