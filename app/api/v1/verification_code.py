from flask import render_template
from flask_mail import Message
from app.api.v1 import api_v1
from app.schemas.verification_code import SendVerificationCodeSchema
from app.extensions import redis_client, mail
from lib.request import load_schema
from lib.response import format
from lib.generate_verification_code import generate_verification_code


@api_v1.post("/verification_code")
def verification_code():
    schema = SendVerificationCodeSchema()
    data = load_schema(schema)

    result = schema.dump(data)
    code = generate_verification_code(6)

    if redis_client.exists(result['key']) == 1:
        return format(message="验证码还在有效时间内")

    if result['purpose'] == 'email_register':
        # TODO 拉黑临时邮箱功能
        msg = Message(recipients=[result['data']])
        msg.subject = "您有新的验证码，请查收"
        msg.html = render_template("otp.html", code=code)
        mail.send(msg)

    redis_client.setex(result['key'], 15 * 60, code)

    return format(message="验证码发送成功")
