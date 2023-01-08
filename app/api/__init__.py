from app.models import User
from app.extensions import jwt, db
from app.schemas.user import UserSchema
from lib import response


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return response.error(message="登录已过期", status_code=401)


@jwt.invalid_token_loader
def invalid_token_callback(cause):
    return response.error(message="Token 未通过验证", status_code=401)


@jwt.unauthorized_loader
def unauthorized_callback(cause):
    return response.error(message="缺少 Authorization Header Token", status_code=401)


@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_payload):
    user = db.session.scalar(db.select(User).filter_by(id=jwt_payload['sub']))
    return UserSchema().dump(user)
