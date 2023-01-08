import urllib
import hashlib
from marshmallow import INCLUDE, fields
from app.schemas import BaseSchema


class UserSchema(BaseSchema):
    class Meta:
        unknown = INCLUDE

    email = fields.Str()
    nickname = fields.Str()
    username = fields.Str()
    gravatar_url = fields.Method('generate_gravatar', dump_only=True)

    def generate_gravatar(self, user):
        url = "https://www.gravatar.com/avatar/" + \
            hashlib.md5(user.email.lower().encode('utf-8')).hexdigest() + "?"
        url += urllib.parse.urlencode({'s': '128'})

        return url
