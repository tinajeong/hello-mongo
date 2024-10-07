from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client.test_database

@app.get("/")
def read_root():
    db.test_collection.insert_one({
        "question": "Which floor is Lyf Funan gym on?",
        "answer": "on the 6th floor."
    })

    result = db.test_collection.find_one({"question": "Which floor is Lyf Funan gym on?"})

    return {
        "question": result['question'],
        "answer": result['answer']
    }
