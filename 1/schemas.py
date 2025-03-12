from marshmallow import Schema, fields, post_load

from .models import Book


class BookSchema(Schema):
    title = fields.Str(required=True, max_length=15)
    author = fields.Str(required=True)

    @post_load
    def make_book(self, data: dict, **kwargs):
        return Book(**data)