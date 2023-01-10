import uuid
from marshmallow import INCLUDE, EXCLUDE, fields
from app.schemas import BaseSchema


class CreateAndResumeSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    slug = fields.Str(load_default=uuid.uuid4().hex)
    layout_type = fields.Str(load_default="style1")
    # TODO 添加默认值
    module_order = fields.Str(load_default="basic")
    theme_color = fields.Str(load_default="#2065d1")
    custom_styles = fields.Dict(allow_none=True)


class ResumeSchema(BaseSchema):
    class Meta:
        unknown = INCLUDE

    name = fields.Str()
    slug = fields.Str()
    layout_type = fields.Str()
    module_order = fields.Str()
    theme_color = fields.Str()
    custom_styles = fields.Dict(allow_none=True)
    user = fields.Nested("UserSchema", only=("id", "username"))
