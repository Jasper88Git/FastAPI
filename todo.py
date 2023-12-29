# curl -X GET http://127.0.0.1:8000/todo -H "accept: application/json" (windows)
# curl -X GET http://127.0.0.1:8000/todo/1 -H "accept: application/json"

# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{}'
# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id":1, "item":"Example schema!"}'
# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id":2, "item":"Validation models help with input types"}'
# curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"item":This todo will be retrieved without exposing my ID!"}'

# curl -X PUT http://127.0.0.1:8000/todo/1 -H "accept: application/json" -H "Content-Type: application/json" -d '{"id":1, "item": "Read the next chapter of the book."}'


# curl -X DELETE http://127.0.0.1:8000/todo/1 -H "accept: application/json"

# APIRouter: 다중라우팅 경로 처리 클래스
# from fastapi import APIRouter
from fastapi import APIRouter, Path
# from model import Todo, TodoItem
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []



# 추가하는 POST 메서드
@todo_router.post("/todo")
# async def add_todo(todo: dict) -> dict:
async def add_todo(todo: Todo) -> dict: # 요청 바디의 변수 유형을 dict -> Todo로 변경
    todo_list.append(todo)
    return {
        "message": "Todo added successfully"
    }


# 조회하는 GET 메서드
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return{
        "todos": todo_list
    }


@todo_router.get("/todo/{todo_id}") # 경로 매개변수 {}
async def get_single_todo(todo_id: int) -> dict: 
    for todo in todo_list:
        if todo.id ==  todo_id:
            return {
                "todo": todo
            }
        return {
            "message": "Todo with supplied ID doesn't exist."
        }
    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict: # Path: 다른 인수와 경로 매개변수를 구분하는 역할
    for todo in todo_list:
        if todo.id ==  todo_id:
            return {
                "todo": todo
            }
        return {
            "message": "Todo with supplied ID doesn't exist."
        }

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

# 기존 ITEM을 변경하는 PUT 메서드
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }

# 기존 ITEM을 삭제하는 DELETE 메서드
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
  for index in range(len(todo_list)):
      todo = todo_list[index]
      if todo.id == todo_id:
          todo_list.pop(index)
          return {
              "message": "Todo deleted successfully."
          }
  return {
      "message": "Todo with supplied ID doesn't exist."
  }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
  todo_list.clear()
  return {
      "message": "Todos deleted successfully."
  }