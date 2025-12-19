
class Cliente:
    def __init__(self,nombre: str, id_cliente: int, activo: bool):
        self.id = id_cliente
        self.nombre = nombre
        self.activo = activo

    def is_active(self) -> bool:
        return self.activo