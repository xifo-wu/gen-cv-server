from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from app.extensions import db
from app.models.base_model_mixin import BaseModelMixin


class User(db.Model, BaseModelMixin):
    email = db.Column(db.String(100))
    nickname = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    mobile = db.Column(db.String(20))

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
