# uvicorn api:app --port 8000 --reload
# uvicorn 파일명:인스턴스 --port 포트번호 (--reload)

from fastapi import FastAPI
from todo import todo_router

app = FastAPI() # 라우트 생성

# curl http://127.0.0.1:8000/
@app.get("/") # 데코레이터 -> 라우트가 호출될 때 실행할 처리
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

# 외부 라우터 추가
app.include_router(todo_router)
