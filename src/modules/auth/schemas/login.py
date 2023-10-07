from apiflask import Schema, fields

class LoginIn(Schema):
    email = fields.String()
    password = fields.String()