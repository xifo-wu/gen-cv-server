from app.extensions import db
from app.models import BaseModelMixin


class ResumeBasicField(db.Model, BaseModelMixin):
    value = db.Column(db.String(255))
    label = db.Column(db.String(255))
    icon = db.Column(db.String(50))
    is_show_label = db.Column(db.Boolean(), default=False)
    is_show_icon = db.Column(db.Boolean(), default=False)
    sort_index = db.Column(db.Float(), default=0.0)
    visible = db.Column(db.Boolean(), default=False)
