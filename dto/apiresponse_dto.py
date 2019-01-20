from time import time
from flask import jsonify


class ApiResponse(object):
    def __init__(self, requestok: bool, success: bool, message: str, request: any, value: any=None) -> None:
        self.requestok = bool(requestok)
        self.success = bool(success) if requestok else False
        self.message = str(message)
        self.request = dict(request)
        self.value = value

    def make_response(self):
        return jsonify({
            'timestamp': time(),
            'success': self.success,
            'message': self.message,
            'request': self.request,
            'value': self.value

        }), self._get_http_statuscode()

    def _get_http_statuscode(self) -> int:
        if not self.requestok:
            return 400
        if not self.success:
            return 500
        return 200
