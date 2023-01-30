from marshmallow import INCLUDE, fields, post_load
from app.models import EducationDetail
from app.schemas import BaseSchema


class EducationDetailSchema(BaseSchema):
    class Meta:
        unknown = INCLUDE

    name = fields.Str()
    start_on = fields.Str()
    end_on = fields.Str()
    university_majors = fields.Str()
    desc = fields.Str()
    sort_index = fields.Float()
    education_id = fields.Int()

    @post_load
    def make_education_detail(self, data, **kwargs):
        return EducationDetail(**data)
