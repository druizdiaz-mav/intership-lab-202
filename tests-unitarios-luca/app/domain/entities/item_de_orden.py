class ItemDeOrden:
    def __init__(self, id_producto: int, cantidad: int, precio_unitario: float = 0.0, id_orden: int = None):
        self.id_orden = id_orden
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        
    def calcular_subtotal(self, exception_to_raise) -> float:
        if self.cantidad <= 0:
            raise exception_to_raise(f"Cantidad inválida en producto {self.id_producto}")
        if self.precio_unitario <= 0:
            raise exception_to_raise(f"Precio inválido en producto {self.id_producto}")
        return self.cantidad * self.precio_unitario
