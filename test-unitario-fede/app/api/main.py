from app.domain.entities import OrdenCompra, ProductoListado
from app.domain.exceptions import ErrorValidacionOrden
from app.application.useCases.validate_order import ValidarOrdenUseCase
from app.infrastructure.repositories.customer_repository import RepositorioClienteMemoria

def main():
    repo = RepositorioClienteMemoria()
    use_case = ValidarOrdenUseCase(repo)

    # Imput simulado
    try:
        id_cliente = 1 
        items = [
            ProductoListado(id_producto=101, cantidad=2, precio=1500, nombre="Teclado Gamer"),
            ProductoListado(id_producto=102, cantidad=1, precio=500, nombre="Mousepad")
        ]
        
        orden = OrdenCompra(id_cliente, items)

        print(f"Procesando orden del cliente {id_cliente}...")
        
        total = use_case.ejecutar(orden)

        print(f"Total a pagar: ${total}")

    except ErrorValidacionOrden as e:
        # 4. MANEJO DE ERRORES DE DOMINIO
        print(f"ERROR DE NEGOCIO: {e}")
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")

if __name__ == "__main__":
    main()