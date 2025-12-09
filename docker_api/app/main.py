from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/hello", response_class=PlainTextResponse, status_code=200)
def read_hello():
    return "Hola"
