from app.domain.entities import OrdenCompra
from app.domain.exceptions import ErrorValidacionOrden
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

class ValidarOrdenUseCase:
    def __init__(self, ClienteRepositorio: RepositorioClienteInterface) -> None:
        self.repositorio = ClienteRepositorio

    def ejecutar(self, orden: OrdenCompra):
        #La OC debe tener Items
        if not orden.productos:
            raise ErrorValidacionOrden("La orden debe tener al menos un producto.")

        #calculo del monto total de la OC
        total = 0.0

        for item in orden.productos:
            
            total += item.cantidad * item.precio

        # El total no puede superar $10.000
        if total > 10000:
            raise ErrorValidacionOrden(f"El total ${total} supera el límite de $10.000.")

        # El cliente debe estar activo
        cliente = self.repositorio.obtener_por_id(orden.id_cliente)
        
        if cliente is None:
            raise ErrorValidacionOrden(f"El cliente {orden.id_cliente} no existe.")

        if not cliente.activo:
            raise ErrorValidacionOrden(f"El cliente {cliente.nombre} no está activo.")

        return total