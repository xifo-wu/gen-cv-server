from marshmallow import EXCLUDE, Schema, ValidationError, fields, validates, validate


class SendVerificationCodeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    purpose = fields.Str(
        required=True,
        validate=validate.OneOf(
            choices=["email_register"], error="必须是: {choices} 之一。"),
        error_messages={
            "required": "用途不能为空",
        }
    )

    data = fields.Str(
        required=True,
        error_messages={
            "required": "数据不能为空",
        }
    )

    key = fields.Method('generate_key')

    def generate_key(self, obj):
        return f"{obj['purpose']}:{obj['data']}"
