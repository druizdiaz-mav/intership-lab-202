from fastapi import HTTPException

from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.domain.customer import Customer

from app.infrastructure.db.session import SessionLocal
from sqlalchemy import select, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Integer)

class PostgresCustomerRepository(CustomerRepositoryInterface):
    def __init__(self, session, logger):
        self.session = session
        self.logger = logger

    def get_customer_by_id(self, customer_id: int) -> Customer:
        stmt = select(CustomerModel).where(CustomerModel.id == customer_id)
        result = self.session.execute(stmt)

        db_customer = result.scalar_one_or_none()

        if db_customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")

        customer = Customer(
            customer_id=db_customer.id,
            name=db_customer.name,
            active=db_customer.active
        )

        return customer