from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1:{"name": "Lucky", "age": 34},
    2:{"name": "Payal", "age": 33},
    3:{"name": "Shreeyan", "age": 1}
}

class User(BaseModel):
    name:str
    age:int

@app.put("/update/{user_id}")
def user_update(user_id:int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return{"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return{"message": "User not found"}

@app.delete('/user/delete/{user_id}')
def user_delete(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return{"message": "User deleted successfully"}
    else:
        return{"message": "User not found"}
    
