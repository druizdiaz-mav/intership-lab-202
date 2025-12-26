from datetime import datetime
from app.domain.entities.item_de_orden import ItemDeOrden
from app.domain.entities.exceptions import DomainException

class Orden:
    def __init__(self, id: int, id_cliente: int, fecha: datetime, items: list[ItemDeOrden], total: float = None):
            self.id = id
            self.id_cliente = id_cliente
            self.fecha = fecha
            self.items = items
            
            # Si viene con el total cargado
            if total is not None:
                self.total = total
            else:
                # Si se debe calcular el total (se envian items en los parametros)
                self.total = sum(item.calcular_subtotal(DomainException) for item in items)