import uuid
from typing import List
from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(..., max_length=15, description="Book title")
    author: str = Field(..., description="Author of the book")


books: List[Book] = [
    Book(title="First Book", author="First Author"),
    Book(title="Second Book", author="Second Author"),
]
