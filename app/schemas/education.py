from marshmallow import INCLUDE, fields, post_load
from app.models.education import Education
from app.schemas import BaseSchema
from app.schemas.education_details import EducationDetailSchema


class EducationSchema(BaseSchema):
    class Meta:
        unknown = INCLUDE

    label = fields.Str()
    value = fields.Str(allow_none=True)
    visible = fields.Bool(default=False, allow_none=True)
    config = fields.Dict(allow_none=True)
    show_split = fields.Bool(default=False, allow_none=True)
    content_type = fields.Str()
    split = fields.Str()
    education_details = fields.List(fields.Nested("EducationDetailSchema"))

    @post_load
    def make_education(self, data, **kwargs):
        return Education(**data)
