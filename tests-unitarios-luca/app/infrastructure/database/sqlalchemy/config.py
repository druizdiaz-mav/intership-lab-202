import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# 1. Leemos las variables directo (Como tu amigo, pero armando la URL async)
# NOTA: Asegúrate de que tu .env tenga DB_USER, DB_PASSWORD, etc.
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mi_db")

# Usamos postgresql+asyncpg (Vital para FastAPI)
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# 2. Creamos el motor ASÍNCRONO (Esto es lo que no puedes negociar)
engine = create_async_engine(DATABASE_URL, echo=True)

# 3. Configuramos la sesión
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# 4. La Base para tus modelos (Tablas)
Base = declarative_base()

# 5. La función simple para usar en tus rutas
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session