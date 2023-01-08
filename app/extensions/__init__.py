from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from app.extensions.redis import RedisClient


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = RedisClient()
ma = Marshmallow()
mail = Mail()
