from app.extensions import db
from app.models import BaseModelMixin


class ResumeBasic(db.Model, BaseModelMixin):
    resume_id = db.Column(db.Integer, db.ForeignKey("resume.id"))
    resume = db.relationship("Resume", back_populates="resume_basic")

    email_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    email = db.relationship(
        "ResumeBasicField",
        backref=db.backref("email", uselist=False),
        cascade="all, delete",
        foreign_keys=[email_id],
    )

    name_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    name = db.relationship(
        "ResumeBasicField",
        backref=db.backref("name", uselist=False),
        cascade="all, delete",
        foreign_keys=[name_id],
    )

    age_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    age = db.relationship(
        "ResumeBasicField",
        backref=db.backref("age", uselist=False),
        cascade="all, delete",
        foreign_keys=[age_id],
    )

    birthday_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    birthday = db.relationship(
        "ResumeBasicField",
        backref=db.backref("birthday", uselist=False),
        cascade="all, delete",
        foreign_keys=[birthday_id],
    )

    avatar_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    avatar = db.relationship(
        "ResumeBasicField",
        backref=db.backref("avatar", uselist=False),
        cascade="all, delete",
        foreign_keys=[avatar_id],
    )

    job_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    job = db.relationship(
        "ResumeBasicField",
        backref=db.backref("job", uselist=False),
        cascade="all, delete",
        foreign_keys=[job_id],
    )

    job_year_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    job_year = db.relationship(
        "ResumeBasicField",
        backref=db.backref("job_year", uselist=False),
        cascade="all, delete",
        foreign_keys=[job_year_id],
    )

    mobile_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    mobile = db.relationship(
        "ResumeBasicField",
        backref=db.backref("mobile_year", uselist=False),
        cascade="all, delete",
        foreign_keys=[mobile_id],
    )

    website_id = db.Column(db.Integer, db.ForeignKey("resume_basic_field.id"))
    website = db.relationship(
        "ResumeBasicField",
        backref=db.backref("website_year", uselist=False),
        cascade="all, delete",
        foreign_keys=[website_id],
    )

    educational_qualifications_id = db.Column(
        db.Integer,
        db.ForeignKey("resume_basic_field.id")
    )
    educational_qualifications = db.relationship(
        "ResumeBasicField",
        backref=db.backref("educational_qualifications_year", uselist=False),
        cascade="all, delete",
        foreign_keys=[educational_qualifications_id],
    )

    in_a_word_id = db.Column(
        db.Integer,
        db.ForeignKey("resume_basic_field.id")
    )
    in_a_word = db.relationship(
        "ResumeBasicField",
        backref=db.backref("in_a_word_year", uselist=False),
        cascade="all, delete",
        foreign_keys=[in_a_word_id],
    )
