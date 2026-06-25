from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Users(BaseModel):
    name:str
    age:int
    city:str

users = []

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def create_users(user:Users):
    users.append(user)
    return {"message":"user created succesfully","user":user}
