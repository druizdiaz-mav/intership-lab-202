from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.application.use_cases.save_orden_uc import SaveOrdenUseCase
from app.application.use_cases.get_orden_uc import GetOrdenUseCase
from app.application.use_cases.delete_orden_uc import DeleteOrdenUseCase

from app.domain.entities.DTOS import CreateOrdenInput, ItemInput
from app.domain.entities.exceptions import DomainException, EntityNotFound

from app.infrastructure.repositories.orden_postgres_repository import OrdenPostgresRepository
from app.infrastructure.repositories.producto_postgres_repository import ProductoPostgresRepository
from app.infrastructure.repositories.cliente_postgres_repository import ClientePostgresRepository
from app.infrastructure.database.sqlalchemy.config import get_db 
from app.api.models import CreateOrdenRequest
from app.infrastructure.database.sqlalchemy.models import OrdenModel, OrdenItemModel

router = APIRouter()

async def get_obtener_orden_use_case(db = Depends(get_db)):
    orden_repo = OrdenPostgresRepository(db)
    return GetOrdenUseCase(orden_repo)

async def get_guardar_orden_use_case(db = Depends(get_db)):
    orden_repo = OrdenPostgresRepository(db)
    producto_repo = ProductoPostgresRepository(db)
    cliente_repo = ClientePostgresRepository(db)
    return SaveOrdenUseCase(orden_repo, producto_repo, cliente_repo)

async def get_borrar_orden_use_case(db = Depends(get_db)):
    orden_repo= OrdenPostgresRepository(db)
    return DeleteOrdenUseCase(orden_repo)

@router.get("/{id}")
async def get_orden(
    id: int,
    use_case: GetOrdenUseCase = Depends(get_obtener_orden_use_case)
):
    try:
        orden = await use_case.execute(id) #Si no encuentra levanta una excepcion

        return {"id": orden.id, "id_cliente": orden.id_cliente, "fecha": orden.fecha, "total": orden.total}
    
    except EntityNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_orden(
    id: int,
    use_case: DeleteOrdenUseCase = Depends(get_borrar_orden_use_case)
):
    try:
        await use_case.execute(id)
        return {"detail": "Orden eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_orden(
    orden_data: CreateOrdenRequest, 
    save_orden_uc: SaveOrdenUseCase = Depends(get_guardar_orden_use_case)
):
    try:
        
        items_dto = [
            ItemInput(id_producto=item.id_producto, cantidad=item.cantidad) 
            for item in orden_data.items
        ]
        
        params = CreateOrdenInput(
            id_cliente=orden_data.id_cliente, 
            items=items_dto
        )
        
        nueva_orden = await save_orden_uc.execute(params)
        
        return {
            "id": nueva_orden.id, 
            "id_cliente": nueva_orden.id_cliente, 
            "fecha": nueva_orden.fecha, 
            "total": nueva_orden.total
        }
        
    except EntityNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
        
    except DomainException as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    except Exception as e:
        print(f"ERROR INTERNO: {e}") 
        raise HTTPException(status_code=500, detail=f"Error del servidor: {str(e)}")
