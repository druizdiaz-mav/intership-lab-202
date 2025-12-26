from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Producto:
    id: int | None
    nombre: str
    precio: float

@dataclass
class Cliente:
    id: int | None
    nombre: str
    activo: bool

@dataclass
class ItemOrden:
    producto_id: int
    cantidad: int
    precio_unitario: float

@dataclass
class Orden:
    id: int | None
    cliente_id: int
    fecha: datetime
    total: float
    items: List[ItemOrden]
