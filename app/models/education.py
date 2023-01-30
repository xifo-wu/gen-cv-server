from app.extensions import db
from app.models import BaseModelMixin


class Education(db.Model, BaseModelMixin):
    resume_id = db.Column(db.Integer, db.ForeignKey("resume.id"))
    resume = db.relationship("Resume", back_populates="education")
    label = db.Column(db.String(255))
    visible = db.Column(db.Boolean(), default=False)
    config = db.Column(db.JSON)
    content_type = db.Column(db.String(50))
    show_split = db.Column(db.Boolean(), default=False)
    split= db.Column(db.String(50))
    education_details = db.relationship("EducationDetail", backref="education")
