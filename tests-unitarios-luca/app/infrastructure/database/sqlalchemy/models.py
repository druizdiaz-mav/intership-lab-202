from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from app.domain.entities.cliente import Cliente 
from app.domain.entities.producto import Producto
from app.domain.entities.orden import Orden
from app.domain.entities.item_de_orden import ItemDeOrden
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

class OrdenModel(Base):
    __tablename__ = "ordenes" 

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    total = Column(Float, nullable=True)
    
    # Mapeo Inverso: De DB a Dominio
    def to_domain(self):
        return Orden(
            id=self.id,
            id_cliente=self.id_cliente,
            fecha=self.fecha,
            items=[], 
            total=self.total 
        )

    # Mapeo Directo: De Dominio a DB (Método estático)
    @staticmethod
    def from_domain(orden):
        return OrdenModel(
            id=orden.id if orden.id != 0 else None,
            id_cliente=orden.id_cliente, 
            fecha= orden.fecha,
            total=orden.total
        )

class OrdenItemModel(Base):
    __tablename__ = "orden_items" 

    id_orden = Column(Integer, nullable=False, primary_key=True)
    id_producto = Column(Integer, nullable=False, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    # Mapeo Inverso: De DB a Dominio
    def to_domain(self):
        return ItemDeOrden(
            id_orden= self.id_orden,
            id_producto= self.id_producto,
            cantidad= self.cantidad,
            precio_unitario= self.precio_unitario
        )
            
        
    # Mapeo Directo: De Dominio a DB (Método estático)
    @staticmethod
    def from_domain(orden_item):
        return OrdenItemModel(
            id=orden_item.id if orden_item.id != 0 else None,
            id_orden=orden_item.id_orden, 
            id_producto=orden_item.id_producto,
            cantidad=orden_itemcantidad,
            precio_unitario=orden_item.precio_unitario
        )