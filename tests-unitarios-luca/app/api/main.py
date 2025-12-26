from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.infrastructure.database.sqlalchemy.config import engine

from app.api.clientes_endpoints import router as clientes_router
from app.api.productos_endpoints import router as productos_router
from app.api.orden_endpoints import router as orden_router

# LIFESPAN (GESTOR DE CICLO DE VIDA)
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose() 

app = FastAPI(
    title="API de Clientes",
    description="Ejemplo de Clean Architecture con FastAPI y SQLAlchemy Async",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
app.include_router(productos_router, prefix="/productos", tags=["Productos"])
app.include_router(orden_router, prefix="/ordenes", tags=["Ordenes"])

@app.get("/")
async def root():
    return {"mensaje": "API FUNCIONANDO"}