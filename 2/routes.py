from typing import Optional, Dict, List

from fastapi import APIRouter, HTTPException, Depends
from .models import Book, books
from .schemas import BookCreate

router = APIRouter()


def get_book_by_id(id: str) -> Optional[Book]:
    for book in books:
        if book.id == id:
            return book
    return None

@router.get("/")
async def index():
    return {"description": "Main page. There is nothing here"}

@router.get("/books", response_model=Dict[str, List[Book]])
async def get_books():
    return {"books": books}

@router.get("/books/{id}", response_model=Book)
async def get_book(id: str):
    book = get_book_by_id(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books", response_model=Book, status_code=201)
async def create_book(book_data: BookCreate):
    book = Book(**book_data.dict())  # Convert input schema to Book model
    books.append(book)
    return book

@router.delete("/books/{id}", status_code=204)
async def delete_book(id: str):
    book = get_book_by_id(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    books.remove(book)
    return {}
