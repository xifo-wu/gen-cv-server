from marshmallow import EXCLUDE, post_load, fields
from app.schemas import BaseSchema
from app.models.resume_basic_field import ResumeBasicField


class ResumeBasicFieldSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    value = fields.Str(allow_none=True)
    label = fields.Str(allow_none=True)
    is_show_label = fields.Bool(default=False, allow_none=True)
    is_show_icon = fields.Bool(default=False, allow_none=True)
    visible = fields.Bool(default=False, allow_none=True)
    sort_index = fields.Float(default=0, allow_none=True)

    @post_load
    def make_resume_basic_field(self, data, **kwargs):
        return ResumeBasicField(**data)
