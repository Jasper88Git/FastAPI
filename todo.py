from fastapi import APIRouter, Path # Path: 다른 인수와 경로 매개변수를 구분하는 역할
from model import Todo

todo_router = APIRouter()

todo_list = []

# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id":1, "item":"First Todo is to finish this book!"}'
# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{}'
# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id":2, "item":"Validation models help with input types"}'
# 추가하는 POST 메서드
@todo_router.post("/todo")
# async def add_todo(todo: dict) -> dict:
async def add_todo(todo: Todo) -> dict: # 요청 바디의 변수 유형을 dict -> Todo로 변경
    todo_list.append(todo)
    return {
        "message": "Todo added successfully"
    }

# curl -X 'GET' 'http://127.0.0.1:8000/todo' -H 'accept: application/json'
# curl -X GET http://127.0.0.1:8000/todo -H "accept: application/json" (windows)
# 조회하는 GET 메서드
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return{
        "todos": todo_list
    }

# curl -X 'GET' 'http://127.0.0.1:8000/todo/1' -H 'accept: application/json'
# @todo_router.get("/todo/{todo_id}") # 경로 매개변수 {}
# async def get_single_todo(todo_id: int) -> dict: 
#     for todo in todo_list:
#         if todo.id ==  todo_id:
#             return {
#                 "todo": todo
#             }
#         return {
#             "message": "Todo with supplied ID doesn't exist."
#         }
    
@todo_router.get("/todo/{todo_id}") # 경로 매개변수 {}
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict: 
    for todo in todo_list:
        if todo.id ==  todo_id:
            return {
                "todo": todo
            }
        return {
            "message": "Todo with supplied ID doesn't exist."
        }

# @todo_router.put("/todo/{todo_id}")
# async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             todo.item = todo_data.item
#             return {
#                 "message": "Todo updated successfully."
#             }
#     return {
#         "message": "Todo with supplied ID doesn't exist."
#     }


# @todo_router.delete("/todo/{todo_id}")
# async def delete_single_todo(todo_id: int) -> dict:
#   for index in range(len(todo_list)):
#       todo = todo_list[index]
#       if todo.id == todo_id:
#           todo_list.pop(index)
#           return {
#               "message": "Todo deleted successfully."
#           }
#   return {
#       "message": "Todo with supplied ID doesn't exist."
#   }

# @todo_router.delete("/todo")
# async def delete_all_todo() -> dict:
#   todo_list.clear()
#   return {
#       "message": "Todos deleted successfully."
#   }
