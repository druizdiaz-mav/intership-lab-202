from app.domain.entities import Orden
from app.domain.exceptions import ErrorValidacionOrden
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface
from app.application.interfaces.orden_repository_interface import RepositorioOrdenInterface

class CrearOrdenUseCase:
    def __init__(self, repo_orden: RepositorioOrdenInterface, repo_cliente: RepositorioClienteInterface):
        self.repo_orden = repo_orden
        self.repo_cliente = repo_cliente

    def ejecutar(self, orden: Orden) -> Orden:
        # Validamo cliente
        cliente = self.repo_cliente.obtener_por_id(orden.cliente_id)
        if not cliente:
            raise ErrorValidacionOrden(f"El cliente {orden.cliente_id} no existe.")
        if not cliente.activo:
            raise ErrorValidacionOrden(f"El cliente {cliente.nombre} no está activo.")

        # Validams orden
        if not orden.items:
            raise ErrorValidacionOrden("La orden debe tener al menos un producto.")

        # Guardamos en SQL
        orden_guardada = self.repo_orden.guardar(orden)
        
        return orden_guardada