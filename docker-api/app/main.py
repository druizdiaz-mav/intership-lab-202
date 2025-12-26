from fastapi import FastAPI
from app.api.endpoints import hello_endpoints

#instancio FastAPI
app = FastAPI()

#registro el router de hello
app.include_router(hello_endpoints.router)

