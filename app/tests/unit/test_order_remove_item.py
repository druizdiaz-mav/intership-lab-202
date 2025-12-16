import pytest

from app.application.usecases.create_order import CreateOrderUseCase
from app.application.usecases.order_add_item import OrderAddItemUseCase
from app.application.usecases.order_remove_item import OrderRemoveItemUseCase

def test_order_remove_item_usecase():
    create_order_usecase = CreateOrderUseCase()
    order = create_order_usecase.execute(customer_id=1)

    order_add_item_usecase = OrderAddItemUseCase(order)
    order_remove_item_usecase = OrderRemoveItemUseCase(order)

    order = order_add_item_usecase.execute(item_id=1, quantity=4)
    order = order_add_item_usecase.execute(item_id=10, quantity=40)
    order = order_add_item_usecase.execute(item_id=15, quantity=20)
    order = order_add_item_usecase.execute(item_id=20, quantity=25)

    order = order_remove_item_usecase.execute(item_id=1, quantity=2)

    assert len(order.items) == 3
    assert 1 in order.items
    assert order.items[1] == 2

    order = order_remove_item_usecase.execute(item_id=10, quantity=2)

    assert len(order.items) == 2
    assert not 1 in order.items

    order = order_remove_item_usecase.execute(item_id=10, quantity=0)

    assert len(order.items) == 1
    assert not 10 in order.items

    order = order_remove_item_usecase.execute(item_id=15, quantity=10)

    assert len(order.items) == 1
    assert 15 in order.items
    assert order.items[15] == 10

    total = 0

    for item_id, qty in order.items.items():
        total += qty

    assert total == 35