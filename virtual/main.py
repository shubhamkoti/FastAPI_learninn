# from fastapi import FastAPI , HTTPException
# from pydantic import BaseModel 

# app = FastAPI()

# class Student(BaseModel):
#     name: str
#     branch: str

# @app.put("/students/{student_id}")
# def update_student(
#     student_id: int,
#     notify: bool = False,
#     student: Student = None
# ):
#     return {
#         "student_id": student_id,
#         "notify": notify,
#         "student": student
#     }


from fastapi import FastAPI , Query , Cookie , Header
from typing import Annotated
from  pydantic import BaseModel

class Item(BaseModel):
  name:str
  description:str| None=None
  price:float
  tax:float | None=None

app=FastAPI()

# @app.put("/items/{item_id}")
# async def update_item(item_id:int , item:Item):
#   return {"Item ":item_id, **item.model_dump()}


# @app.get("/item")
# async def read_item(q:Annotated[str| None, Query(min_length=3,max_length=50,pattern="^fixquery$")]=None):
#   results={"Items":[{"item_id":"Foo"},{"item_id":"Bae"}]}
#   if q:
#     results.update({"q":q})
#   return results

# @app.get("/item")
# async def read_items(q:Annotated[list[str]| None,Query()]=None):
#   query_items={"q":q}
#   return query_items
# He manje apn default values set krnya sathi ahe , ani baki sudha 

class Item(BaseModel):
  name:str
  description:str | None= None
  price:float
  tax:float|None=None
  
class User(BaseModel):
  username:str
  dull_name:str | None= None

@app.put("/item/{item_id}")
async def update_item(item_id:int , item:Item , user:User):
  results={"Item_id":item_id , "Item":item, "user":user}
  return results

# Cookies 
@app.get("/item")
async def read_item(ads:Annotated[str|None,Header()]=None):
  return {"Id":ads}