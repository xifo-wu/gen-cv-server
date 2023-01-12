import time
from flask_jwt_extended import get_jwt, get_jwt_identity, create_access_token, create_refresh_token, jwt_required, get_current_user

from app.api.v1 import api_v1
from app.extensions import db, redis_client
from app.models.user import User
from app.schemas.auth import PasswordLoginSchema, RegisterSchema
from app.schemas.user import UserSchema
from lib.request import load_schema
from lib import response

user_schema = UserSchema()
register_schema = RegisterSchema()
password_login_schema = PasswordLoginSchema()


@api_v1.post('/register')
def register():
    """
    当前只允许 Email 验证码注册
    """
    data = load_schema(register_schema)

    user = User(
        username=data['email'],
        nickname=data['email'],
        email=data['email'],
        password=data['password'],
    )

    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)
    meta = dict()
    meta['access_token'] = create_access_token(identity=result['id'])
    meta['refresh_token'] = create_refresh_token(identity=result['id'])

    return response.format(data=result, meta=meta)


@api_v1.post('/login')
def login():
    """
    当前只支持用户名密码登录
    """
    data = load_schema(password_login_schema)

    # 经过 Schema 验证 user 一定存在
    user = db.session.scalar(
        db.select(User).filter_by(username=data['username']))
    result = user_schema.dump(user)

    meta = dict()
    meta['access_token'] = create_access_token(identity=result['id'])
    meta['refresh_token'] = create_refresh_token(identity=result['id'])

    return response.format(data=result, meta=meta)


@api_v1.delete('/logout')
@jwt_required()
def logout():
    jwt = get_jwt()
    exp = jwt['exp'] - int(time.time())
    redis_client.set(jwt['jti'], "", ex=exp)
    return response.format(message="退出登录成功")


@api_v1.get('/user')
@jwt_required()
def current_user():
    user = get_current_user()
    return response.format(data=user)


@api_v1.post('/refresh-token')
@jwt_required()
def refresh_token():
    identity = get_jwt_identity()

    meta = dict()
    meta['access_token'] = create_access_token(identity=identity)

    return response.format(meta=meta)
