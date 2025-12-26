from fastapi import APIRouter
from pydantic import BaseModel

from app.application.usecases.get_customer_by_id import GetCustomerByIdUseCase

class CustomerSchema(BaseModel):
    id: int
    name: str
    active: bool

def create_customer_repository_router(get_customer_by_id: GetCustomerByIdUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/customer/{customer_id}")
    def get_customer(customer_id: int) -> CustomerSchema:
        customer = get_customer_by_id.execute(customer_id)

        return CustomerSchema(
            id=customer.get_id(),
            name=customer.get_name(),
            active=customer.is_active()
        )

    return router