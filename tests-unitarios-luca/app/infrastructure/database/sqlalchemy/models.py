from sqlalchemy import Column, Integer, String, Boolean, Float
from app.domain.entities.cliente import Cliente 
from app.domain.entities.producto import Producto
from app.infrastructure.database.sqlalchemy.config import Base 

class ClienteModel(Base):
    __tablename__ = "clientes" 

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    
    # Mapeo Inverso: De DB a Dominio
    def to_domain(self):
        return Cliente(id=self.id, nombre=self.nombre, activo=self.activo)

    # Mapeo Directo: De Dominio a DB (Método estático)
    @staticmethod
    def from_domain(cliente):
        return ClienteModel(
            id=cliente.id if cliente.id != 0 else None,
            nombre=cliente.nombre, 
            activo=cliente.activo
        )

class ProductoModel(Base):
    __tablename__ = "productos" 

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    
    # Mapeo Inverso: De DB a Dominio
    def to_domain(self):
        return Producto(id=self.id, nombre=self.nombre, precio=self.precio)
    # Mapeo Directo: De Dominio a DB (Método estático)
    @staticmethod
    def from_domain(producto):
        return ProductoModel(
            id=producto.id if producto.id != 0 else None,
            nombre=producto.nombre, 
            precio=producto.precio
        )