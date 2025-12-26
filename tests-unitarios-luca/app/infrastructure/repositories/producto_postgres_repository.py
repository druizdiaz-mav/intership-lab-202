from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.infrastructure.database.sqlalchemy.models import ProductoModel
from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.domain.entities.producto import Producto

class ProductoPostgresRepository(ProductoRepositoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, producto: Producto) -> Producto:
        #Convertir Dominio -> Modelo DB
        producto_model = ProductoModel.from_domain(producto)
        self.db.add(producto_model)
        await self.db.commit()
        await self.db.refresh(producto_model)
        return producto_model.to_domain()

    async def get_by_id(self, id: int) -> Producto:
        result = await self.db.execute(
            select(ProductoModel).where(ProductoModel.id == id)
        )
        producto_model = result.scalar_one_or_none()
        if producto_model:
            return producto_model.to_domain()
        return None

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(
            select(ProductoModel).where(ProductoModel.id == id)
        )
        producto_model = result.scalar_one_or_none()

        # Si existe devuelve true
        if producto_model:
            await self.db.delete(producto_model)
            await self.db.commit()
            return True

        #Si no existe devuelve false
        return False