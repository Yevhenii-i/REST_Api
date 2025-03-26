from typing import Dict, Union

from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError

from .models import Book, books
from .schemas import BookSchema

main = Blueprint('main', __name__)


def make_response(data: Union[Dict, Book], status_code: int = 200):
    return jsonify(data), status_code

def get_book_by_id(id) -> Union[Book, None]:
    for book in books:
        if book.id == id:
            return book


@main.route('/')
def index():
    return make_response("description", "Main page. There is nothing here")

@main.route('/books', methods=['GET'])
def get_books():
    return make_response({"books": books})

@main.route('/books/<string:id>', methods=['GET'])
def get_book(id):
    book = get_book_by_id(id)
    if not book:
        return abort(404)
    return make_response({"book": book})

@main.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    try:
        book_schema = BookSchema()
        book = book_schema.load(data)
    except ValidationError as err:
        return make_response({"error": err.messages}, 422)
    books.append(book)
    return make_response({"book": book}, 201)

@main.route('/books/<string:id>', methods=['DELETE'])
def delete_book(id: str):
    book = get_book_by_id(id)
    if not book:
        return abort(404)
    books.remove(book)
    return make_response({}, 204)

