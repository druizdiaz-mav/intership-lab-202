import logging

from fastapi import FastAPI

from app.application.usecases.validate_order import ValidateOrderUseCase
from app.application.usecases.order_add_item import OrderAddItemUseCase
from app.application.usecases.order_remove_item import OrderRemoveItemUseCase
from app.application.usecases.create_order import CreateOrderUseCase
from app.application.usecases.get_customer_by_id import GetCustomerByIdUseCase
from app.application.usecases.get_item_by_id import GetItemByIdUseCase
from app.application.routers.customer_repository_router import create_customer_repository_router
from app.application.routers.item_repository_router import create_item_repository_router
from app.infrastructure.repositories.customer_repository import MockCustomerRepository
from app.infrastructure.repositories.item_repository import MockItemRepository
from app.domain.customer import Customer
from app.domain.order import Order
from app.domain.item import Item

def create_application() -> FastAPI:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    app = FastAPI()

    # Setup repositories
    customer_repository = MockCustomerRepository()
    item_repository = MockItemRepository()

    # Setup routers
    get_customer_by_id_usecase = GetCustomerByIdUseCase(customer_repository)
    get_item_by_id_usecase = GetItemByIdUseCase(item_repository)

    customer_router = create_customer_repository_router(get_customer_by_id_usecase)
    item_router = create_item_repository_router(get_item_by_id_usecase)
    app.include_router(customer_router)
    app.include_router(item_router)

    # Create a new order
    create_order_usecase = CreateOrderUseCase()
    order = create_order_usecase.execute(customer_id=1)

    # Add items to the order
    order_add_item_usecase = OrderAddItemUseCase(order)
    order = order_add_item_usecase.execute(item_id=52, qty=2)
    order = order_add_item_usecase.execute(item_id=53, qty=1)

    # Remove an item from the order
    order_remove_item_usecase = OrderRemoveItemUseCase(order)
    order = order_remove_item_usecase.execute(item_id=52, qty=1)
    # Validate the order
    validate_order_usecase = ValidateOrderUseCase(customer_repository, item_repository)
    is_valid = validate_order_usecase.execute(order)

    logger.info(f"Order valid: {is_valid}")
    logger.info(f"Order details: Customer ID - {order.customer_id}, Items - {order.items}")

    return app

app = create_application()