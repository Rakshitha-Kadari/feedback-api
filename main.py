from fastapi import FastAPI
from pydantic import BaseModel
import json
import os 

# Initialize FastAPI app
app = FastAPI()

# Define the structure of the incoming feedback
class Feedback(BaseModel):
    name: str
    email: str
    message: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Feedback API!"}    

# POST endpoint to receive feedback
@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    feedback_data = feedback.dict()
    file_path = "feedback.json"

    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            data = json.load(f)
    else:
        data=[]

    data.append(feedback_data)

    with open(file_path,"w") as f:
        json.dump(data, f, indent=4)  

    return {
        "message": "Feedback received successfully ✅",
        "data": feedback
    }
