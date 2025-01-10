from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=True)
    email = fields.String(required=True)

class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_name = fields.String(required=True)
    price = fields.Float(required=True)
    description = fields.String()

class OrderSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    order_date = fields.DateTime(dump_only=True)
    user_id = fields.Integer(required=True)
    status = fields.String(required=True)

class OrderProductSchema(ma.Schema):
    order_id = fields.Integer()
    product_id = fields.Integer()
