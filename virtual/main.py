from fastapi import FastAPI 

app=FastAPI()

@app.get('/')
def home():
  return {"message":"this is About page"}

@app.get("/about")
def about():
  return {"Message" :"this is about page"}

@app.get("/users")
def user():
  return {"users":["Mohit","shubh"]}


@app.get("/login")
def login():
  return {
    "name":"javir",
    "age":24,
    "Skills":["C++","Python"]
  }