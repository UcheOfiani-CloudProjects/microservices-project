from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "User service is running"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}
