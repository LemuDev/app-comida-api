from apiflask import Schema, fields
from apiflask.fields import Nested


class RestaurantOut(Schema):
    id = fields.Integer()
    name = fields.String()
    description: fields.String()
    user_id: fields.Integer()

class RestaurantsOut(Schema):
    data = fields.List(Nested(RestaurantOut))
    next_page = fields.String()
    prev_page = fields.String()
    

