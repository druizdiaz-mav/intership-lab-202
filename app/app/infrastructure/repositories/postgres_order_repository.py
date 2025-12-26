from fastapi import HTTPException

from app.application.interfaces.order_repository_interface import OrderRepositoryInterface
from app.domain.order import Order

from app.infrastructure.db.session import SessionLocal
from sqlalchemy import select, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OrderModel(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    total = Column(Float)

class PostgresOrderRepository(OrderRepositoryInterface):
    def __init__(self, session, logger):
        self.session = session
        self.logger = logger

    def get_order_by_id(self, order_id: int) -> Order:
        stmt = select(OrderModel).where(OrderModel.id == order_id)
        result = self.session.execute(stmt)

        db_order = result.scalar_one_or_none()

        if db_order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        order = Order(
            order_id=db_order.id,
            customer_id=db_order.customer_id,
            total=db_order.total
        )

        return order

    def add_order(self, order: Order) -> Order:
        db_order = OrderModel(
            customer_id=order.customer_id,
            total=order.total
        )

        self.logger.info(f"Adding order for customer ID: {order.customer_id} with total: {order.total}")

        self.session.add(db_order)
        self.session.commit()

        order.order_id = db_order.id

        return order

    def remove_order(self, order_id: int):
        stmt = select(OrderModel).where(OrderModel.id == order_id)
        result = self.session.execute(stmt)

        db_order = result.scalar_one_or_none()

        if db_order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        self.session.delete(db_order)
        self.session.commit()