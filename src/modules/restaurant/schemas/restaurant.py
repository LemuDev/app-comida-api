from apiflask import Schema, fields
from apiflask.fields import Nested


class RestaurantOut(Schema):
    name = fields.String()
    description: fields.String()
    user_id: fields.Integer()

class RestaurantsOut(Schema):
    data = fields.List(Nested(RestaurantOut))
    num_pages = fields.Integer()
    current_pages = fields.Integer()
    

