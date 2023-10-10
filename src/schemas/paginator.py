from apiflask import Schema, fields

class PaginatorQuery(Schema):
    page = fields.Integer(default=1)
    rows_per_page = fields.Integer(default=10)
    