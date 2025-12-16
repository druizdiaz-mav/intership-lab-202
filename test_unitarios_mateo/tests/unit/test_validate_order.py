import pytest
from unittest.mock import Mock
from app.domain.entities import Order, Item
from app.domain.exceptions import InvalidOrderException
from app.application.useCases.validate_order import ValidateOrderUseCase

@pytest.fixture
def mock_customer_repo():
    repo = Mock()
    repo.is_active.return_value = True
    return repo

def test_order_valida_retorna_total(mock_customer_repo):
    items = [Item("Producto1", 2, 100), Item("Producto2", 1, 50)]
    order = Order(customer_id=1, items=items)
    use_case = ValidateOrderUseCase(mock_customer_repo)

    total = use_case.execute(order)
    assert total == 250

def test_orden_sin_items_genera_error(mock_customer_repo):
    order = Order(customer_id=1, items=[])
    use_case = ValidateOrderUseCase(mock_customer_repo)
    with pytest.raises(InvalidOrderException, match="al menos un ítem"):
        use_case.execute(order)

def test_cliente_inactivo_genera_error(mock_customer_repo):
    mock_customer_repo.is_active.return_value = False
    items = [Item("Producto1", 1, 100)]
    order = Order(customer_id=1, items=items)
    use_case = ValidateOrderUseCase(mock_customer_repo)
    with pytest.raises(InvalidOrderException, match="no está activo"):
        use_case.execute(order)

def test_cantidad_invalida_genera_error(mock_customer_repo):
    items = [Item("Producto1", 0, 100)]
    order = Order(customer_id=1, items=items)
    use_case = ValidateOrderUseCase(mock_customer_repo)
    with pytest.raises(InvalidOrderException, match="cantidad del ítem"):
        use_case.execute(order)

def test_precio_unitario_invalido_genera_error(mock_customer_repo):
    items = [Item("Producto1", 1, 0)]
    order = Order(customer_id=1, items=items)
    use_case = ValidateOrderUseCase(mock_customer_repo)
    with pytest.raises(InvalidOrderException, match="precio unitario del ítem"):
        use_case.execute(order)

def test_total_mayor_10000_genera_error(mock_customer_repo):
    items = [Item("Producto1", 100, 200)]
    order = Order(customer_id=1, items=items)
    use_case = ValidateOrderUseCase(mock_customer_repo)
    with pytest.raises(InvalidOrderException, match="no puede superar los"):
        use_case.execute(order)
