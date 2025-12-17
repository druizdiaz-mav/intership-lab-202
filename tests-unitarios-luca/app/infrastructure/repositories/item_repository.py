from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.entities import Producto

lista_productos = [
    Producto(1, "Producto A", 10.0),
    Producto(2, "Producto B", 20.0),
    Producto(3, "Producto C", -30.0),
]

class ItemRepositoryInMemory(ItemRepositoryInterface):
    def get_price(self, item_id: int) -> float:
        for producto in lista_productos:
            if producto.id == item_id:
                return producto.precio
        return None