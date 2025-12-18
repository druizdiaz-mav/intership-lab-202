from fastapi import FastAPI
from app.api.endpoints.hello_endpoint import router as hello_router

app = FastAPI()
app.include_router(hello_router)