from app.domain.exceptions import ErrorValidacionOrden
from datetime import datetime
from typing import List

#Se define al cliente
class Cliente:
    def __init__(self, id: int, nombre: str, activo: bool):
        self.id = id
        self.nombre = nombre
        self.activo = activo

#Se define el producto
class Producto:
    def __init__(self, id: int, descripcion: str, precio_actual: int):
        if precio_actual < 0:
            raise ErrorValidacionOrden(f"El precio no puede ser menos a 0")
        
        self.id = id
        self.descripcion = descripcion
        self.precio_actual = precio_actual

#se definen las propiedades para que el producto pueda ser agregado a la OC
class ItemOrden:
    def __init__(self, producto_id: int, cantidad: int, precio_unitario: int):
        if cantidad <= 0:
            raise ErrorValidacionOrden(f"La cantidad debe ser mayor a 0")
        
        if precio_unitario <= 0:
            raise ErrorValidacionOrden(f"El precio debe ser mayor a 0")
        
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario


#Se define la orden de compra. Como producto solo toma una lista en la que cada elemento sea un objeto de la clase ProductoListado
class Orden: 
    def __init__(self, id: int, cliente_id: int, items: List[ItemOrden], fecha: datetime = None, total: float = 0.0):
        self.id = id
        self.cliente_id = cliente_id
        self.items = items
        self.fecha = fecha if fecha else datetime.now()
        if total > 0:
             self.total = total
        else:
             self.total = sum(item.cantidad * item.precio_unitario for item in items)



