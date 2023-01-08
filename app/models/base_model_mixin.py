from datetime import datetime
from app.extensions import db


class BaseModelMixin:
    time_now = datetime.utcnow
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=time_now)
    updated_at = db.Column(db.DateTime, onupdate=time_now)
