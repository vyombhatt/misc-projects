from marshmallow import Schema, fields

class ItemSchema(Schema):
    # id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)