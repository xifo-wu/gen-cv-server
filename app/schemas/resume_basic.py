from marshmallow import EXCLUDE, post_load, fields
from app.schemas import BaseSchema
from app.schemas.resume_basic_field import ResumeBasicFieldSchema
from app.models.resume_basic import ResumeBasic


class ResumeBasicSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    name = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    age = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    birthday = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    avatar = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    job = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    job_year = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    mobile = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    website = fields.Nested("ResumeBasicFieldSchema", allow_none=True)
    educational_qualifications = fields.Nested(
        "ResumeBasicFieldSchema", allow_none=True)
    in_a_word = fields.Nested("ResumeBasicFieldSchema", allow_none=True)

    @post_load
    def make_resume_basic(self, data, **kwargs):
        return ResumeBasic(**data)
