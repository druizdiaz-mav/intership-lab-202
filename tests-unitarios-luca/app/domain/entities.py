class Persona:
    dni: int
    nombre: str
    estado: str
    def __init__(self,nombre, id_cliente, estado):
        self.id = id_cliente
        self.nombre = nombre
        self.estado = estado

class Producto:
    nombre:str
    precio: float
    def __init__(self, id_producto, nombre, precio):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio

class LineaDeOrden:
    id_producto: int
    cantidad: int
    def __init__(self, id_producto, cantidad):
        self.id_producto = id_producto
        self.cantidad = cantidad

class Orden:
    id_persona: int
    lineas_de_orden: list
    def __init__(self, id_persona, lineas_de_orden):
        self.id_persona = id_persona
        self.lineas_de_orden = lineas_de_orden # lista de lineas_de_orden
