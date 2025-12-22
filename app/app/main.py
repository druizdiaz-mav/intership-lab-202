import logging

from fastapi import FastAPI

from app.application.usecases.validate_order import ValidateOrderUseCase
from app.application.usecases.order_add_item import OrderAddItemUseCase
from app.application.usecases.order_remove_item import OrderRemoveItemUseCase
from app.application.usecases.create_order import CreateOrderUseCase
from app.application.usecases.get_customer_by_id import GetCustomerByIdUseCase
from app.application.usecases.get_item_by_id import GetItemByIdUseCase
from app.application.usecases.get_order_by_id import GetOrderByIdUseCase
from app.application.usecases.repository_add_order import RepositoryAddOrderUseCase
from app.application.usecases.repository_remove_order import RepositoryRemoveOrderUseCase
from app.application.usecases.calculate_order_total import CalculateOrderTotalUseCase
from app.application.routers.customer_repository_router import create_customer_repository_router
from app.application.routers.item_repository_router import create_item_repository_router
from app.application.routers.order_repository_router import create_order_repository_router
from app.infrastructure.repositories.mock_customer_repository import MockCustomerRepository
from app.infrastructure.repositories.mock_item_repository import MockItemRepository
from app.infrastructure.repositories.mock_order_repository import MockOrderRepository
from app.infrastructure.repositories.postgres_customer_repository import PostgresCustomerRepository
from app.infrastructure.repositories.postgres_item_repository import PostgresItemRepository
from app.infrastructure.repositories.postgres_order_repository import PostgresOrderRepository
from app.domain.customer import Customer
from app.domain.order import Order
from app.domain.item import Item

from app.infrastructure.db.session import SessionLocal

def create_application() -> FastAPI:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Create a new database session
    session = SessionLocal()
    app = FastAPI()

    # Setup repositories
    customer_repository = PostgresCustomerRepository(session, logger)
    item_repository = PostgresItemRepository(session, logger)
    order_repository = PostgresOrderRepository(session, logger)

    # Setup routers
    get_customer_by_id_usecase = GetCustomerByIdUseCase(customer_repository)
    get_item_by_id_usecase = GetItemByIdUseCase(item_repository)
    get_order_by_id_usecase = GetOrderByIdUseCase(order_repository)

    customer_router = create_customer_repository_router(get_customer_by_id_usecase)
    item_router = create_item_repository_router(get_item_by_id_usecase)
    order_router = create_order_repository_router(get_order_by_id_usecase)
    app.include_router(customer_router)
    app.include_router(item_router)
    app.include_router(order_router)

    # Create a new order
    create_order_usecase = CreateOrderUseCase()
    order = create_order_usecase.execute(customer_id=1)

    # Add items to the order
    order_add_item_usecase = OrderAddItemUseCase(order)
    order = order_add_item_usecase.execute(item_id=1, qty=2)
    order = order_add_item_usecase.execute(item_id=2, qty=1)

    # Remove an item from the order
    order_remove_item_usecase = OrderRemoveItemUseCase(order)
    order = order_remove_item_usecase.execute(item_id=1, qty=1)

    # Validate the order
    validate_order_usecase = ValidateOrderUseCase(customer_repository, item_repository)
    is_valid = validate_order_usecase.execute(order)

    if (is_valid):
        calculate_order_total_usecase = CalculateOrderTotalUseCase(item_repository)
        order = calculate_order_total_usecase.execute(order)

        repository_add_order_usecase = RepositoryAddOrderUseCase(order_repository)
        order = repository_add_order_usecase.execute(order)

        logger.info(f"Order details: Customer ID - {order.customer_id} total - {order.total}")
        logger.info(f"Order added with ID: {order.order_id}")
    else:
        logger.error("Order is not valid")

    return app

app = create_application()