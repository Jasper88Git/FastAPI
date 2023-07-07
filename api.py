# uvicorn api:app --port 8000 --reload (file:instace)

from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

# curl http://127.0.0.1:8000/
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }


app.include_router(todo_router)