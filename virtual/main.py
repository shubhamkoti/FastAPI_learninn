from fastapi import FastAPI 

app=FastAPI()

@app.get('/user')
def home(name):
  return {"Name":name}


@app.get('/products')
def get_users(limit:int=10):
  return {
    "Limit":limit
  }


# Multiple parameters 

@app.get("/items")
def items(name:str=None,price:int=0):
  return {
     "Name":name,
     "price":price
  }