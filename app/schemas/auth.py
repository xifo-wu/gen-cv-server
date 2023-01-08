from marshmallow import EXCLUDE, INCLUDE, Schema, validates_schema, ValidationError, fields, validates, validate
from app.extensions import db, redis_client
from app.models import User


class PasswordLoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.Str(
        required=True,
        error_messages={
            "required": "用户名不能为空"
        }
    )

    password = fields.Str(
        required=True,
        error_messages={
            "required": "密码不能为空"
        }
    )

    @validates_schema
    def validate_username_and_password(self, data, **kwargs):
        u = db.session.scalar(
            db.select(User).filter_by(username=data['username']))

        if u is None:
            raise ValidationError(message="用户不存在", field_name="username")

        if not u.validate_password(data['password']):
            raise ValidationError(message="密码不正确", field_name="pasword")


class RegisterSchema(Schema):
    class Meta:
        unknown = INCLUDE

    email = fields.Email(
        error_messages={
            "invalid": "邮箱格式不正确"
        }
    )

    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=8, error="密码必须大于 {min} 位"),
        error_messages={
            "required": "密码不能为空",
        }
    )

    registration_method = fields.Str(
        required=True,
        validate=validate.OneOf(
            choices=["email_register"], error="必须是: {choices} 之一。"),
        error_messages={
            "required": "注册方式不能为空",
        }
    )

    verification_code = fields.Str()

    @validates("email")
    def validate_eamil(self, value):
        u = db.session.scalar(db.select(User).filter_by(email=value))
        if u is not None:
            raise ValidationError("邮箱已被占用")

    @validates_schema
    def validate_verification_code(self, data, **kwargs):
        # 当注册方法是邮箱注册时
        if data['registration_method'] == 'email_register':
            if data.get('email') is None:
                raise ValidationError("邮箱不能为空", field_name="email")
            if data.get('verification_code') is None:
                raise ValidationError(
                    "验证码不能为空", field_name="verification_code")

            code = redis_client.get(
                f"{data['registration_method']}:{data['email']}").decode('utf-8')

            if data['verification_code'] != code:
                raise ValidationError("验证码不正确", field_name="verification_code")
