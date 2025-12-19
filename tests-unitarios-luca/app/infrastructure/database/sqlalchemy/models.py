from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ClienteModel(Base):
    __tablename__ = "clientes" # Tabla creada en el init

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    
    # Mapeo Inverso: De DB a Dominio
    def to_domain(self):
        from domain.entities.cliente import Cliente
        return Cliente(id=self.id, nombre=self.nombre, activo=self.activo)

    # Mapeo Directo: De Dominio a DB (Método estático)
    @staticmethod
    def from_domain(cliente):
        return ClienteModel(
            id=cliente.id, 
            nombre=cliente.nombre, 
            activo=cliente.activo
        )