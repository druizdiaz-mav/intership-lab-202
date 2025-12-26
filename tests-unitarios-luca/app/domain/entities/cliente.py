
class Cliente:
    def __init__(self,nombre: str, id: int, activo: bool):
        self.id = id
        self.nombre = nombre
        self.activo = activo

    def is_active(self) -> bool:
        return self.activo