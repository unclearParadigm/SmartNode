from flask import request
from flask import jsonify
from flask import Blueprint
from backend import configuration

from backend.models.getrequest import GetRequest
from backend.models.setrequest import SetRequest
from backend.models.apiresponse import ApiResponse

hal = configuration.get_hal()
getsetapi = Blueprint('getset_api', __name__)


@getsetapi.route('/api/node/set', methods=['POST'])
def _set() -> object:
    request_body = request.get_json(silent=True, cache=False, force=False)
    set_request = SetRequest.create(request_body)

    if set_request is None:
        return ApiResponse(False, False, 'Invalid request, Schema Validation failed', request_body).make_response()

    if set_request.mode not in hal.SUPPORTED_OUTPUT_MODES:
        return ApiResponse(True, False, 'Hardware does not support the specified mode', request_body).make_response()

    if not hal.set(set_request):
        return ApiResponse(True, False, 'Could not set', request_body).make_response()

    return ApiResponse(True, True, 'OK', request_body).make_response()


@getsetapi.route('/api/node/get/<int:gpio>', methods=['GET'])
def _get(gpio: int) -> object:
    get_request = GetRequest(int(gpio))
    success, read_value = hal.get(get_request)

    if not success:
        return ApiResponse(True, False, 'Could not get value', get_request.__dict__).make_response()

    return jsonify(read_value.__dict__), 200
