# DTOs de entrada (Input Port)
class ItemInput:
    def __init__(self, id_producto: int, cantidad: int):
        self.id_producto = id_producto
        self.cantidad = cantidad

class CreateOrdenInput:
    def __init__(self, id_cliente: int, items: list[ItemInput]):
        self.id_cliente = id_cliente
        self.items = items