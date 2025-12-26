from fastapi import HTTPException

from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.item import Item

from app.infrastructure.db.session import SessionLocal
from sqlalchemy import select, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    price = Column(Float)

class PostgresItemRepository(ItemRepositoryInterface):
    def __init__(self, session, logger):
        self.session = session
        self.logger = logger

    def get_item_by_id(self, item_id: int) -> Item:
        stmt = select(ItemModel).where(ItemModel.id == item_id)
        result = self.session.execute(stmt)

        db_item = result.scalar_one_or_none()

        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")

        item = Item(
            item_id=db_item.id,
            description=db_item.description,
            price=db_item.price
        )

        return item