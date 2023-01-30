from app.extensions import db
from app.models import BaseModelMixin


class EducationDetail(db.Model, BaseModelMixin):
    name = db.Column(db.String(255))
    start_on = db.Column(db.String(255))
    end_on = db.Column(db.String(255))
    university_majors = db.Column(db.String(255))
    desc = db.Column(db.Text)
    sort_index = db.Column(db.Float(), default=0.0)
    education_id = db.Column(db.Integer, db.ForeignKey("education.id"))

