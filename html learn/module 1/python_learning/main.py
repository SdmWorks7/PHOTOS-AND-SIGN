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

@app.delete("/users/{user_id}")
def remove_user(user_id:int):
    db=SessionLocal()
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        db.close()
        return {"error":"user not found"}
    db.delete(user)
    db.commit()
    db.close()
    return {"message":"user deleted successfully!"}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UserInput):
    db=SessionLocal()
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        db.close()
        return {"error":"user not found"}
    user.name = updated_user.name
    user.age = updated_user.age
    user.city = updated_user.city
    db.commit()
    db.close()
    return {"message":"user updated successfully!"}
    
    