from pydantic import BaseModel
from typing import List
from datetime import datetime

# DTO para recibir un Item desde el JSON
class ItemOrdenDTO(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class ItemOrdenResponseDTO(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float
    
    class Config:
        from_attributes = True # Permite leer desde objetos clase 


# DTO para recibir la Orden completa
class OrdenCreateDTO(BaseModel):
    cliente_id: int
    items: List[ItemOrdenDTO]

class OrdenResponseDTO(BaseModel):
    id: int
    cliente_id: int
    fecha: datetime
    total: float
    items: List[ItemOrdenResponseDTO] # Lista anidada

    class Config:
        from_attributes = True


# PRODUCTOS
class ProductoCreateDTO(BaseModel):
    descripcion: str
    precio_actual: float

class ProductoResponseDTO(BaseModel):
    id: int
    descripcion: str
    precio_actual: float
    class Config:
        from_attributes = True


# CLIENTES
class ClienteCreateDTO(BaseModel):
    nombre: str
    activo: bool

class ClienteResponseDTO(BaseModel):
    id: int
    nombre: str
    activo: bool
    class Config:
        from_attributes = True