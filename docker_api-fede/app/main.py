from fastapi import FastAPI
from app.api.endpoint import hello

app = FastAPI(title="Clean Architecture Demo")

# Incluimos las rutas definidas en la capa de API
app.include_router(hello.router)


#uvicorn app.main:app --reload