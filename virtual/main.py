from fastapi import FastAPI 

app=FastAPI()


@app.get("/users/{user_id}")
def user(user_id):
  return {"users":user_id}

