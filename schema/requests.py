set_schema = {
    "$id": "SmartHomeNode_HTTP-POST_REQUEST_Json_Body",
    "$schema": "http://json-schema.org/draft-07/schema#",

    "type": "object",
    "properties": {
        "session": {
            "type": "string",
            "minLength": 32,
            "description": "session token"
        },
        "mode": {
            "type": "string",
            "minLength": 3,   # pwm
            "maxLength": 7,   # digital
            "description": "describes which actor shall be controlled"
        },
        "actor": {
            "type": "integer",
            "minimum": 0,
            "maximum": 256,
            "description": "the id of the actor that shall be used (e.g. Pin-Number)"
        },
        "value": {
            "type": "integer",
            "minimum": 0,
            "maximum": 1024,
            "description": "The value that shall be set on the specified actor"
        }
    },

    "required": [
        "session", "output", "actor", "value"
    ]
}