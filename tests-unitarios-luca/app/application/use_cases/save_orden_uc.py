from app.application.interfaces.orden_repository_interface import OrdenRepositoryInterface
from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.orden import Orden
from app.domain.entities.item_de_orden import ItemDeOrden as OrdenItem
from app.domain.entities.DTOS import CreateOrdenInput
from app.domain.entities.exceptions import DomainException
from datetime import datetime

class SaveOrdenUseCase:

    def __init__(self, 
                 orden_repo: OrdenRepositoryInterface, 
                 producto_repo: ProductoRepositoryInterface,
                 cliente_repo: ClienteRepositoryInterface):
        self.orden_repo = orden_repo
        self.producto_repo = producto_repo
        self.cliente_repo = cliente_repo
    
    async def execute(self, params: CreateOrdenInput) -> Orden:
        # Validar Cliente usando el REPOSITORIO
        await self.validar_cliente(params.id_cliente)
        
        items_dominio = []
        
        for item_in in params.items:
            producto = await self.producto_repo.get_by_id(item_in.id_producto)
            
            if not producto:
                raise DomainException(f"Producto {item_in.id_producto} no encontrado.")

            nuevo_item = OrdenItem(
                id_producto=producto.id,
                cantidad=item_in.cantidad,
                precio_unitario=producto.precio 
            )
            items_dominio.append(nuevo_item)

        # La Orden calcula su propio total al recibir los items en el init
        nueva_orden = Orden(
            id=0,
            id_cliente=params.id_cliente,
            fecha= datetime.utcnow(),
            items=items_dominio
        )
        
        saved_orden = await self.orden_repo.save(nueva_orden)
        
        return saved_orden

    async def validar_cliente(self, id_cliente: int):
        cliente = await self.cliente_repo.get_by_id(id_cliente)
        if not cliente:
             raise DomainException(f"Cliente {id_cliente} no encontrado o inactivo.")