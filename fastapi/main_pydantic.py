from fastapi import FastAPI 
from pydantic import BaseModel , Field , EmailStr, HttpUrl , SecretStr 
from enum import Enum 
from datetime import date 

app=FastAPI()

students={
     1: {"name":"shubham"},
     2: {"Name":"patil"},
     3: {"namr":"koti"}
}

@app.get("/students")
def student():
  return students


@app.get("/students/{students_id}")
def get_std(students_id:int):
  return students.get(
    students_id,
    {"erro":"std not found"}
  )


# Optional Query Parameters
# Sometimes users don't provide a value.
@app.get("/jobs")
def get_jobs(location: str = None,company: str = None,page: int = 1):
    return {
        "location": location,
        "company": company,
        "page": page
    }

# /jobs 
# /jobs?location=pune
# /jobs?company=Google


# Both can be implemented in one route below is ex
@app.get("/studen")
def get_students(page: int):
    return {"page": page}

# /students?page=2


# **************************Pydantic use *****************************
# from pydantic import BaseModel , Field
from typing import Optional
class Student(BaseModel):
   name:str
   age: int 
   city: Optional[str]=None    # optional Field 
   Country : str="India"     # default Values 
 
class StudentRegister(BaseModel):
   name: str=Field(
          min_length=4,
          max_length=30,
          description="Enter Student's Full Name",
          exmple=[" Shubham Koti"]
   )
   age : int=Field(
      ge=18,
      le=60,
      description="Age should be btw 18-60"
   )
   password:str=Field(
      min_length=8,
      description="Password Should be minimum of 8 Characters"
   )


@app.post("/register")
def register(student: StudentRegister):
   return student


  #  -----------Advance Pydantic --------
# from enum import Enum
# from datetime import date
# from pydantic import EmailStr , HttpUrl , SecretStr

class Branch(str, Enum):
   CSE="CSE",
   IT = "IT",
   ENTC="ENTC"

class Studentregister(BaseModel):
   full_name:str
   email:EmailStr
   password:SecretStr
   github:HttpUrl
   dob:date
   branch:Branch

@app.post("/advance")
def validate(detail:Studentregister):
   return detail