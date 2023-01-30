from app.extensions import db
from app.models import BaseModelMixin
from app.models.education import Education


class Resume(db.Model, BaseModelMixin):
    name = db.Column(db.String(20))
    slug = db.Column(db.String(50))
    layout_type = db.Column(db.String(50))
    module_order = db.Column(db.String(255))
    theme_color = db.Column(db.String(50))
    custom_styles = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="user")

    resume_basic = db.relationship(
        "ResumeBasic",
        back_populates="resume",
        cascade="all, delete-orphan",
        uselist=False,
        lazy="joined"
    )

    education: Education = db.relationship(
        "Education",
        back_populates="resume",
        cascade="all, delete-orphan",
        uselist=False,
        lazy="joined"
    )
