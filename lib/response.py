from flask import jsonify


def api_request_error(e):
    return jsonify(e.to_dict()), e.status_code


def format(data=None, message=None, meta=None, success=True):
    result = {
        "success": success,
    }

    if data is not None:
        result["data"] = data

    if message is not None:
        result["message"] = message

    if meta is not None:
        result["meta"] = meta

    return jsonify(result), 200


def error(message=None, meta=None, success=False, status_code=400):
    result = {
        "success": success,
    }

    if message is not None:
        result["message"] = message

    if meta is not None:
        result["meta"] = meta

    return jsonify(result), status_code
