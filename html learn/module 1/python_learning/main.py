from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, User

app = FastAPI()

class UserInput(BaseModel):
    name: str
    age: int
    city: str

@app.get("/users")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}

@app.post("/users")
def create_user(user: UserInput):
    db = SessionLocal()
    new_user = User(name=user.name, age=user.age, city=user.city)
    db.add(new_user)
    db.commit()
    db.close()
    return {"message": "User created!"}
