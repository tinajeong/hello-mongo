from fastapi import FastAPI
from pymongo import MongoClient
import gradio as gr

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client.test_database
db.test_collection.insert_one({
    "question": "Which floor is Lyf Funan gym on?",
    "answer": "on the 6th floor."
})


def get_answer(question: str):
    result = db.test_collection.find_one({"question": question})
    if result:
        return result["answer"]
    else:
        return "Sorry, I don't have an answer for that question."

def gradio_interface(question: str):
    return get_answer(question)

gr_interface = gr.Interface(fn=gradio_interface, inputs="text", outputs="text", title="MongoDB With Q&A")

@app.get("/")
def read_root():
    return {"message": "FastAPI with MongoDB!!"}

@app.get("/gradio")
def gradio_launch():
    return gr_interface.launch(share=True)
