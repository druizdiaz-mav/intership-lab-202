import pytest

from app.application.usecases.create_order import CreateOrderUseCase
from app.application.usecases.order_add_item import OrderAddItemUseCase

def test_order_add_item_usecase():
    create_order_usecase = CreateOrderUseCase()
    order = create_order_usecase.execute(customer_id=1)

    order_add_item_usecase = OrderAddItemUseCase(order)

    order = order_add_item_usecase.execute(item_id=1, quantity=2)

    assert len(order.items) == 1
    assert 1 in order.items
    assert order.items[1] == 2

    order = order_add_item_usecase.execute(item_id=50, quantity=20)

    assert len(order.items) == 2
    assert 50 in order.items
    assert order.items[50] == 20

    total = 0

    for item_id, qty in order.items.items():
        total += qty

    assert total == 22