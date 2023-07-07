# uvicorn api:app --port 8000 --reload
# uvicorn 파일명:인스턴스 --port 포트번호 (--reload)

from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

# curl http://127.0.0.1:8000/
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

app.include_router(todo_router) # 외부 라우터 추가git commit -m "Resolve merge conflicts"
