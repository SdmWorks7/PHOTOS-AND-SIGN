from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Hello World!"}

@app.get("/greet/{name}")
def greet(name:str):
    return {"message":f"Hello {name}"}

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Saumyadeep", "city": "Jamshedpur"},
        {"id": 2, "name": "Rahul", "city": "Mumbai"},
        {"id": 3, "name": "Priya", "city": "Delhi"}
    ]
    return {"users": users}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = [
        {"id": 1, "name": "Saumyadeep", "city": "Jamshedpur"},
        {"id": 2, "name": "Rahul", "city": "Mumbai"},
        {"id": 3, "name": "Priya", "city": "Delhi"}
    ]
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"error": "User not found"}
