from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.infrastructure.database.sqlalchemy.models import OrdenModel, OrdenItemModel
from app.application.interfaces.orden_repository_interface import OrdenRepositoryInterface
from app.domain.entities.orden import Orden

class OrdenPostgresRepository(OrdenRepositoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, orden: Orden) -> Orden:
        orden_model = OrdenModel.from_domain(orden)
        self.db.add(orden_model)
        await self.db.flush()
        for item in orden.items:
                item_db = OrdenItemModel(
                    id_orden=orden_model.id,
                    id_producto=item.id_producto,
                    cantidad=item.cantidad,
                    precio_unitario=item.precio_unitario
                )
                self.db.add(item_db)
            
        await self.db.commit()
        await self.db.refresh(orden_model)
        return orden_model.to_domain()

    async def get_by_id(self, id: int) -> Orden:
        query = select(OrdenModel).where(OrdenModel.id == id)
        result = await self.db.execute(query)
        orden_model = result.scalar_one_or_none()
        if orden_model:
            return orden_model.to_domain()
        return None
    
    async def delete(self, id: int) -> bool:
        query = select(OrdenModel).where(OrdenModel.id == id)
        result = await self.db.execute(query)
        orden_model = result.scalar_one_or_none()

        # Si existe devuelve true
        if orden_model:
            await self.db.delete(orden_model)
            await self.db.commit()
            return True
        
        # Si no existe devuelve falase
        return False