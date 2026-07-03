from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# Hite apn scheme jya nusar banvaycha ahe techa nusar class declare kela eh , 
# manje apn validation hite check krto type of name , age , manually check nahi karav lagat hya madhe jr Pydantic use krto asel tr 

# class User(BaseModel):
#   name:str
#   age:int
#   email:str


# @app.post("/create-user")
# def create_user(user:User):
#   return {
#     "Message":"User Created",
#     "users": user
#   }

# class Address(BaseModel):
#    city:str
#    pincode:int

# class User(BaseModel):
#    name:str
#    age:int 
#    address:Address

# @app.post("/create-user")
# def create(user:User):
#    return {
#       "Message":"Created User",
#       "user":User
#    }



# -----------CRUD ------------
todos=[]

class Todo(BaseModel):
  id:int 
  title: str
  completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
  todos.append(todo)
  return {
    "Message":"Todo Added ", "data":todo
  }

@app.get("/todos")
def get_todos():
  return todos

# here we get element with particular ID 
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
  for todo in todos:
    if todo.id  == todo_id:
     return todo
    
  return {"error ": "todo not foinud "}
 
# here we update the old value
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int ,updated_todo:Todo):
  for index,todo in enumerate(todos):
    if todo.id ==todo_id:
      todos[index]=updated_todo
      return {
        "Message ":"data updated",
        "Data":updated_todo
      }
    
  return { "erro":"Todos not found"}