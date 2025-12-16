import pytest
from app.domain.entities import Orden, LineaDeOrden
from app.domain.exceptions import InvalidOrderException
from app.application.useCases.validate_order import ValidateOrderUseCase

from app.infrastructure.repositories.customer_repository import CustomerRepositoryInMemory
from app.infrastructure.repositories.item_repository import ItemRepositoryInMemory

@pytest.fixture
def use_case():
    # Instanciamos los repositorios en memoria
    repo_clientes = CustomerRepositoryInMemory()
    """
    lista_personas = [
    Persona("Luca", 1, "activo"),
    Persona("Fede", 2, "inactivo"),
    Persona("Mateo", 3, "activo"),
    Persona("Licha", 4, "inactivo"),
    ]
    """
    repo_items = ItemRepositoryInMemory()
    """
    lista_productos = [
    Producto(1, "Producto A", 10.0),
    Producto(2, "Producto B", 20.0),
    Producto(3, "Producto C", -30.0),
    ]
    """
    
    # Inyeccion de dependencias
    return ValidateOrderUseCase(repo_clientes, repo_items)

def test_orden_valida_retorna_total(use_case):
    orden = Orden(1, [LineaDeOrden(1, 2)]) # 2 * 10.0 = 20.0
    total = use_case.execute(orden)
    assert total == 20.0

def test_orden_sin_lineas_retorna_error(use_case):
    orden = Orden(1, [])
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)

def test_cliente_inactivo_error(use_case):
    orden = Orden(2, [LineaDeOrden(1, 1)])
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)

def test_cantidad_invalida_error(use_case):
    orden = Orden(1, [LineaDeOrden(1, 0)])
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)

def test_item_no_existente_error(use_case):
    orden = Orden(1, [LineaDeOrden(999, 1)])
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)

def test_item_con_precio_negativo_error(use_case):
    orden = Orden(1, [LineaDeOrden(3, 1)])
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)

def test_total_excede_limite_error(use_case):
    orden = Orden(1, [LineaDeOrden(2, 600)])  # 600 * 20.0 = 12000.0
    with pytest.raises(InvalidOrderException):
        use_case.execute(orden)