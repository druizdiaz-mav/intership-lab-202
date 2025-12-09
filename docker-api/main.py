from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def read_hello():
    return JSONResponse(content={"message": "Hello"}, status_code=200)