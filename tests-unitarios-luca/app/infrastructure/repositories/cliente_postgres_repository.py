from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.infrastructure.database.sqlalchemy.models import ClienteModel
from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.cliente import Cliente

# Esta clase IMPLEMENTA el contrato del dominio usando SQLAlchemy
class ClientePostgresRepository(ClienteRepositoryInterface):
    
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, cliente: Cliente) -> Cliente:
        #Convertir Dominio -> Modelo DB
        cliente_db = ClienteModel.from_domain(cliente)
        
        #Guardar en SQL
        self.db.add(cliente_db)
        await self.db.commit()
        await self.db.refresh(cliente_db)
        
        #Convertir Modelo DB -> Dominio y devolver
        return cliente_db.to_domain()

    async def get_by_id(self, id: int):
        query = select(ClienteModel).where(ClienteModel.id == id)
        result = await self.db.execute(query)
        return result.scalars().one_or_none()

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ClienteModel).where(ClienteModel.id == id))
        #Convierte las tuplas resultantes en instancias del modelo
        cliente_db = result.scalars().one_or_none()
        
        # Si existe se borra y devuelve true
        if cliente_db:
            await self.db.delete(cliente_db)
            await self.db.commit()
            return True
            
        # Si no existe devolvemos false
        return False