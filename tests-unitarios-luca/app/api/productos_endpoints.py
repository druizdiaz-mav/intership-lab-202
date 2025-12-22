from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.producto import Producto
from app.application.use_cases.get_producto_uc import GetProductoUseCase
from app.application.use_cases.save_producto_uc import SaveProductoUseCase
from app.application.use_cases.delete_producto_uc import DeleteProductoUseCase
from app.infrastructure.repositories.productos_postgres_repository import ProductosPostgresRepository 
from app.infrastructure.database.sqlalchemy.config import get_db 

router = APIRouter()

async def get_obtener_producto_use_case(db: AsyncSession = Depends(get_db)):
    # Creamos el Repositorio con la sesión inyectada
    repo = ProductosPostgresRepository(db)
    
    # Devolvemos el Caso de Uso listo
    return GetProductoUseCase(repo)

async def get_guardar_producto_use_case(db: AsyncSession = Depends(get_db)):
    repo = ProductosPostgresRepository(db)

    return SaveProductoUseCase(repo)

async def get_eliminar_producto_use_case(db: AsyncSession = Depends(get_db)):
    repo = ProductosPostgresRepository(db)
    
    return DeleteProductoUseCase(repo)

@router.get("/{id}")
async def get_producto(
    id: int,
    use_case: GetProductoUseCase = Depends(get_obtener_producto_use_case) 
):
    try:

        producto = await use_case.execute(id)
        
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        return {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_producto(
    nombre: str,
    precio: float,
    use_case: SaveProductoUseCase = Depends(get_guardar_producto_use_case)
):
    try:
        nuevo_producto = Producto(nombre=nombre, id=0, precio = precio)
        producto_guardado = await use_case.execute(nuevo_producto)
        return {"id": producto_guardado.id, "nombre": producto_guardado.nombre, "precio": producto_guardado.precio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_producto(
    id: int,
    use_case: DeleteProductoUseCase = Depends(get_eliminar_producto_use_case)
):
    try:
        await use_case.execute(id)
        return {"detail": "Producto eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))