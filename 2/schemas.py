from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(..., max_length=15, description="Title of the book")
    author: str = Field(..., description="Author of the book")
