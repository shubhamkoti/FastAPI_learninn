from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# Hite apn scheme jya nusar banvaycha ahe techa nusar class declare kela eh , 
# manje apn validation hite check krto type of name , age , manually check nahi karav lagat hya madhe jr Pydantic use krto asel tr 
class User(BaseModel):
  name:str
  age:int

@app.post("/create-user")
def create_user(user:User):
  return {
    "users": user
  }