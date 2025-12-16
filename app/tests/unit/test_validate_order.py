import pytest

from app.application.usecases.create_order import CreateOrderUseCase
from app.application.usecases.order_add_item import OrderAddItemUseCase
from app.application.usecases.order_remove_item import OrderRemoveItemUseCase
from app.application.usecases.validate_order import ValidateOrderUseCase
from app.infrastructure.repositories.customer_repository import MockCustomerRepository
from app.infrastructure.repositories.item_repository import MockItemRepository

def test_validate_order_usecase():
    create_order_usecase = CreateOrderUseCase()
    order = create_order_usecase.execute(customer_id=1)

    order_add_item_usecase = OrderAddItemUseCase(order)
    order_remove_item_usecase = OrderRemoveItemUseCase(order)

    customer_repository = MockCustomerRepository()
    item_repository = MockItemRepository()

    # No items in the order
    validate_order_usecase = ValidateOrderUseCase(customer_repository, item_repository)

    assert validate_order_usecase.execute(order) == False

    # Add valid items
    order = order_add_item_usecase.execute(item_id=10, quantity=5)
    order = order_add_item_usecase.execute(item_id=20, quantity=3)

    assert validate_order_usecase.execute(order) == True

    # Test invalid items
    order = order_add_item_usecase.execute(item_id=30, quantity=0)

    assert validate_order_usecase.execute(order) == False

    order = order_remove_item_usecase.execute(item_id=30, quantity=0)
    order = order_add_item_usecase.execute(item_id=0, quantity=10)

    assert validate_order_usecase.execute(order) == False

    order = order_remove_item_usecase.execute(item_id=0, quantity=0)

    # Add an item with a very high qty (order >= $10,000)
    order = order_add_item_usecase.execute(item_id=30, quantity=10000)

    assert validate_order_usecase.execute(order) == False

    order = order_remove_item_usecase.execute(item_id=30, quantity=9999)

    assert validate_order_usecase.execute(order) == True

    # Test inactive customer
    order = create_order_usecase.execute(customer_id=2)

    assert validate_order_usecase.execute(order) == False