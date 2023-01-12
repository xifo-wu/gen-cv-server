from marshmallow import EXCLUDE, fields
from app.schemas import BaseSchema


class ResumeBasicFieldSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    value = fields.Str()
    label = fields.Str()
    laiconyout_type = fields.Str()
    is_show_label = fields.Bool()
    is_show_icon = fields.Bool()
    visible = fields.Bool()
    sort_index = fields.Float()
