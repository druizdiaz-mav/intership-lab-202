from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

# Definimos el endpoint 
@app.get("/hello", response_class=PlainTextResponse, status_code=200)
def read_root():
    return "Hola"