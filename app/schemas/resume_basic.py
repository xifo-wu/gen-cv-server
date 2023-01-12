from marshmallow import EXCLUDE, fields
from app.schemas import BaseSchema
from app.schemas.resume_basic_field import ResumeBasicFieldSchema


class ResumeBasicSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Nested("ResumeBasicFieldSchema")
    name = fields.Nested("ResumeBasicFieldSchema")
    age = fields.Nested("ResumeBasicFieldSchema")
    birthday = fields.Nested("ResumeBasicFieldSchema")
    avatar = fields.Nested("ResumeBasicFieldSchema")
    job = fields.Nested("ResumeBasicFieldSchema")
    job_year = fields.Nested("ResumeBasicFieldSchema")
    mobile = fields.Nested("ResumeBasicFieldSchema")
    website = fields.Nested("ResumeBasicFieldSchema")
    educational_qualifications = fields.Nested("ResumeBasicFieldSchema")
    in_a_word = fields.Nested("ResumeBasicFieldSchema")
