from app.domain.exceptions import ErrorValidacionOrden

#Se define al cliente
class Cliente:
    def __init__(self, id: int, nombre: str, activo: bool):
        self.id = id
        self.nombre = nombre
        self.activo = activo

#Se define el producto
class Producto:
    def __init__(self, id: int, descripcion: str, precio_actual: int):
        self.id = id
        self.descripcion = descripcion
        self.precio_actual = precio_actual

#se definen las propiedades para que el producto pueda ser agregado a la OC
class ProductoListado:
    def __init__(self, id_producto: int, cantidad: int, precio: int, nombre:str):
        if cantidad <= 0:
            raise ErrorValidacionOrden(f"El producto {nombre} tiene cantidad inválida.")
        
        if precio <= 0:
            raise ErrorValidacionOrden(f"El producto {nombre} tiene precio inválido.")
        
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio = precio
        self.nombre = nombre

    
#Se define la orden de compra. Como producto solo toma una lista en la que cada elemento sea un objeto de la clase ProductoListado
class OrdenCompra: 
    def __init__(self, id_cliente: int, productos: list[ProductoListado]):
        self.id_cliente = id_cliente
        self.productos = productos



