from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.entities.cliente import Cliente
from domain.repositories.cliente_repository import ClienteRepository
from infrastructure.database.sqlalchemy.models import ClienteModel

# Esta clase IMPLEMENTA el contrato del dominio usando SQLAlchemy
class PostgresClienteRepository(ClienteRepository):
    
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, cliente: Cliente) -> Cliente:
        # 1. Convertir Dominio -> Modelo DB
        cliente_db = ClienteModel.from_domain(cliente)
        
        # 2. Guardar en SQL
        self.db.add(cliente_db)
        await self.db.commit()
        await self.db.refresh(cliente_db)
        
        # 3. Convertir Modelo DB -> Dominio y devolver
        return cliente_db.to_domain()

    async def get_by_id(self, id: int) -> Cliente | None:
        result = await self.db.execute(select(ClienteModel).where(ClienteModel.id == id))
        cliente_db = result.scalars().first()
        
        if cliente_db:
            return cliente_db.to_domain()
        return None