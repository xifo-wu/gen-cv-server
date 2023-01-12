from flask import Blueprint
from lib import response
from app.models import User
from app.schemas.user import UserSchema
from app.extensions import jwt, db, redis_client
from app.api.v1 import api_v1

api = Blueprint('api', __name__)
api.register_blueprint(api_v1, url_prefix='/v1')
# 开启支持 subdomain
# api.register_blueprint(api_v1, url_prefix='/v1', subdomain='api')


@api.errorhandler(500)
def internal_server_error(e):
    return response.error(message="服务器出错", status_code=500)


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


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return response.error(message="登录已过期", status_code=401)


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    # 检查redis块列表中是否存在JWT的回调函数
    jti = jwt_payload["jti"]
    token_in_redis = redis_client.get(jti)
    return token_in_redis is not None
