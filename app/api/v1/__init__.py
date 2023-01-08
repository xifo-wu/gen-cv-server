from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

if __name__ == 'app.api.v1':
    from app.api.v1 import auth, verification_code
