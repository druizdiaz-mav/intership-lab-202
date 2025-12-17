import pytest
from unittest.mock import MagicMock
from app.domain.entities import OrdenCompra, ProductoListado, Cliente
from app.domain.exceptions import ErrorValidacionOrden
from app.application.useCases.validate_order import ValidarOrdenUseCase
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

@pytest.fixture
def mock_repo():
    # Creamos un repositorio falso y Le decimos que respete la interfaz RepositorioClienteInterface
    return MagicMock(spec=RepositorioClienteInterface)

@pytest.fixture
def use_case(mock_repo):
    # Inyectamos el repositorio falso al caso de uso
    return ValidarOrdenUseCase(mock_repo)



def test_orden_valida_retorna_total_correcto(use_case, mock_repo):

    mock_repo.obtener_por_id.return_value = Cliente(id=1, nombre="Cliente Test", activo=True)
    
    items = [
        ProductoListado(id_producto=101, cantidad=2, precio=1000, nombre="Teclado"), # 2000
        ProductoListado(id_producto=102, cantidad=1, precio=500, nombre="Mouse")     # 500
    ]
    orden = OrdenCompra(id_cliente=1, productos=items)

    # Ejecutamos
    total = use_case.ejecutar(orden)

    # Verificamos
    assert total == 2500  # Verificamos la suma
    mock_repo.obtener_por_id.assert_called_once_with(1) # Verificamos que llamó al repo


def test_error_orden_sin_productos(use_case):
    # Intentamos pasar una lista vacía
    orden = OrdenCompra(id_cliente=1, productos=[])

    # Esperamos que lance la excepción con el mensaje correcto
    with pytest.raises(ErrorValidacionOrden, match="debe tener al menos un producto"):
        use_case.ejecutar(orden)

def test_error_cantidad_invalida(use_case):
    # Producto con cantidad 0
    items = [ProductoListado(101, 0, 100, "Licuadora")]
    orden = OrdenCompra(id_cliente=1, productos=items)

    with pytest.raises(ErrorValidacionOrden, match="cantidad inválida"):
        use_case.ejecutar(orden)

def test_error_precio_invalido(use_case):
    # Producto con precio negativo
    items = [ProductoListado(101, 1, -500, "Monitor")]
    orden = OrdenCompra(id_cliente=1, productos=items)

    with pytest.raises(ErrorValidacionOrden, match="precio inválido"):
        use_case.ejecutar(orden)

def test_error_total_supera_limite(use_case):
    # Producto que cuesta 15.000 (el límite es 10.000)
    items = [ProductoListado(101, 1, 15000, "Pc  gamer completa")]
    orden = OrdenCompra(id_cliente=1, productos=items)

    with pytest.raises(ErrorValidacionOrden, match="supera el límite"):
        use_case.ejecutar(orden)


def test_error_cliente_inactivo(use_case, mock_repo):
    # Configuramos el mock para que devuelva un cliente con activo=False
    cliente_inactivo = Cliente(id=2, nombre="Cacho", activo=False)
    mock_repo.obtener_por_id.return_value = cliente_inactivo
    
    items = [ProductoListado(101, 1, 100, "Notebook")]
    orden = OrdenCompra(id_cliente=2, productos=items)

    with pytest.raises(ErrorValidacionOrden, match="no está activo"):
        use_case.ejecutar(orden)


#python -m pytest tests/unit/test_validate_order.py