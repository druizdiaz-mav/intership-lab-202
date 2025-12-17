from enum import Enum

class Persona:
    def __init__(self,nombre: str, id_cliente: int, estado: EstadoPersona):
        self.id = id_cliente
        self.nombre = nombre
        self.estado = estado

    def is_active(self) -> bool:
        return self.estado == EstadoPersona.ACTIVO

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio

class LineaDeOrden:
    def __init__(self, id_producto: int, cantidad: int, precio_unitario: float = 0.0):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    def calcular_subtotal(self, exception_to_raise) -> float:
        if self.cantidad <= 0:
            raise exception_to_raise(f"Cantidad inválida en producto {self.id_producto}")
        if self.precio_unitario <= 0:
            raise exception_to_raise(f"Precio inválido en producto {self.id_producto}")
        return self.cantidad * self.precio_unitario

class Orden:
    def __init__(self, id_persona: int, lineas_de_orden: list[LineaDeOrden]):
        self.id_persona = id_persona
        self.lineas_de_orden = lineas_de_orden # lista de lineas_de_orden
    def calcular_total(self, exception_to_raise) -> float:
        total = sum(linea.calcular_subtotal(exception_to_raise) for linea in self.lineas_de_orden)

        if total > 10000:
            raise exception_to_raise("El total excede el límite permitido.")
        
        return total

class EstadoPersona(Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"