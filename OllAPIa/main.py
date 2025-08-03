from fastapi import FastAPI
from api import chat

app = FastAPI()


@app.get("/")
def read_root():
    return "Hi, I'm OllAPIa!"


@app.post("/chat")
def chat_with_user(prompt: str):
    return chat(prompt)
