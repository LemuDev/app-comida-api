from apiflask import Schema, fields
from apiflask.validators import Length, Email

class RegisterIn(Schema):
    first_name = fields.String(required=True, validate=[Length(min=1), Length(max=60)])
    last_name = fields.String(required=True, validate=[Length(min=1), Length(max=60)])
    email = fields.String(required=True, validate=[Length(min=1), Length(max=100), Email()])
    password = fields.String(required=True, validate=[Length(min=1), Length(max=100)])
    