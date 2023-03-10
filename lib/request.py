from marshmallow import Schema, ValidationError
from flask import request
from lib.api_exception import APIParamsValidationError, APIBadRequestError


def load_schema(schema: Schema, **kwargs):
    try:
        payload = request.get_json()
    except BaseException:
        raise APIBadRequestError()

    try:
        data = schema.load(payload, **kwargs)
    except ValidationError as err:
        raise APIParamsValidationError(errors=err)

    return data
