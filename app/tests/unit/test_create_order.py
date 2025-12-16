import pytest

from app.application.usecases.create_order import CreateOrderUseCase

def test_create_order_usecase():
    create_order_usecase = CreateOrderUseCase()

    order = create_order_usecase.execute(customer_id=1)

    assert order.get_customer_id() == 1
    assert order.get_items() == {}