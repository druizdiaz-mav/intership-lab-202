from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.cliente import Cliente
from app.application.use_cases.get_cliente_uc import GetClienteUseCase
from app.application.use_cases.save_cliente_uc import SaveClienteUseCase
from app.application.use_cases.delete_cliente_uc import DeleteClienteUseCase
from app.infrastructure.repositories.clientes_postgres_repository import ClientePostgresRepository 
from app.infrastructure.database.sqlalchemy.config import get_db 

router = APIRouter()

async def get_obtener_cliente_use_case(db: AsyncSession = Depends(get_db)):
    # Creamos el Repositorio con la sesión inyectada
    repo = ClientePostgresRepository(db)
    
    # Devolvemos el Caso de Uso listo
    return GetClienteUseCase(repo)

async def get_guardar_cliente_use_case(db: AsyncSession = Depends(get_db)):
    repo = ClientePostgresRepository(db)
    
    return SaveClienteUseCase(repo)

async def get_eliminar_cliente_use_case(db: AsyncSession = Depends(get_db)):
    repo = ClientePostgresRepository(db)
    
    return DeleteClienteUseCase(repo)

@router.get("/{id}")
async def get_cliente(
    id: int,
    use_case: GetClienteUseCase = Depends(get_obtener_cliente_use_case) 
):
    try:

        cliente = await use_case.execute(id)
        
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")

        return {"id": cliente.id, "nombre": cliente.nombre, "activo": cliente.activo}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_cliente(
    nombre: str,
    use_case: SaveClienteUseCase = Depends(get_guardar_cliente_use_case)
):
    try:
        nuevo_cliente = Cliente(nombre=nombre, id=0, activo=True)
        cliente_guardado = await use_case.execute(nuevo_cliente)

        return {"id": cliente_guardado.id, "nombre": cliente_guardado.nombre, "activo": cliente_guardado.activo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_cliente(
    id: int,
    use_case: DeleteClienteUseCase = Depends(get_eliminar_cliente_use_case)
):
    try:
        await use_case.execute(id)
        return {"detail": "Cliente eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))