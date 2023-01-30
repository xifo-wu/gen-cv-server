from marshmallow import Schema, fields, post_dump, pre_load


class BaseSchema(Schema):
    # SKIP_VALUES = set([None])

    id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # @post_dump
    # def remove_skip_values(self, data, **kwargs):
    #     return {
    #         key: value for key, value in data.items() if value not in self.SKIP_VALUES
    #     }

    # @pre_load
    # def remove_skip_values(self, data, **kwargs):
    #     print(data)
    #     # for key, value in data.items():
    #         # if value not in self.SKIP_VALUES:
    #         #     print(key)

    #     # return data
    #     return {
    #         key: value for key, value in data.items()
    #         if value not in self.SKIP_VALUES
    #     }
