from marshmallow import ValidationError


class APIRequestError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class APIBadRequestError(APIRequestError):
    status_code = 400
    message = "请求解析错误，请确认请求格式是否正确。上传文件请使用 multipart 标头，参数请使用 JSON 格式。"

    def __init__(self, message=None):
        self.payload = {
            "success": False,
            "code": 40000,
        }

        if message is not None:
            self.message = message


class APIParamsValidationError(APIRequestError):
    status_code = 422
    message = "数据未通过验证"

    def __init__(self, errors=ValidationError):
        # 处理错误格式
        for value in errors.messages.values():
            self.message = value[0]
            break

        self.payload = {
            "success": False,
            "code": 40022,
        }
