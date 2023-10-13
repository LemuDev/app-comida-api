from apiflask import Schema, fields
from apiflask.fields import Nested
from apiflask.validators import Length


class RestaurantOut(Schema):
    id = fields.Integer()
    name = fields.String()
    description: fields.String()
    user_id: fields.Integer()

class RestaurantsOut(Schema):
    data = fields.List(Nested(RestaurantOut))
    next_page = fields.String()
    prev_page = fields.String()
    

class RestaurantIn(Schema):
    name = fields.String(validate=[Length(max=60)], required=True)
    description = fields.String(validate=[Length(max=255)], required=True)
    image = fields.File(required=True)