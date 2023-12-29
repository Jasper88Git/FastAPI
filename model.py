from pydantic import BaseModel

class PacktBook(BaseModel):
    id: int
    Name: str
    Publishers: str
    Isbn: str

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }

class TodoItem(BaseModel):
    item: str
  
    class Config:
        schema_extra = {
            "example": {
            "item": "Read the next chapter of the book"
        }  
    }
