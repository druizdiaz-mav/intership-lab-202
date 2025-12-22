from fastapi import FastAPI, HTTPException
from app.infrastructure.repositories.customer_repository import RepositorioClienteSQL
from app.infrastructure.repositories.order_repository import RepositorioOrdenSQL 
from app.application.useCases.create_order import CrearOrdenUseCase
from app.application.useCases.get_order import ObtenerOrdenUseCase 
from app.domain.entities import Orden, ItemOrden
from app.domain.exceptions import ErrorValidacionOrden
from app.api.schemas import OrdenCreateDTO
from app.api.schemas import OrdenResponseDTO 
from app.infrastructure.repositories.product_repository import RepositorioProductoSQL
from app.application.useCases.create_product import CrearProductoUseCase
from app.application.useCases.create_customer import CrearClienteUseCase
from app.api.schemas import ProductoCreateDTO, ProductoResponseDTO, ClienteCreateDTO, ClienteResponseDTO
from app.domain.entities import Producto, Cliente
from app.application.useCases.delete_customer import EliminarClienteUseCase
from app.application.useCases.delete_product import EliminarProductoUseCase
from app.application.useCases.delete_order import EliminarOrdenUseCase
from app.application.useCases.get_cliente import ObtenerClienteUseCase
from app.application.useCases.get_product import ObtenerProductoUseCase

app = FastAPI()


# Instanciamos las implementaciones SQL 
repo_cliente = RepositorioClienteSQL()
repo_orden = RepositorioOrdenSQL()
repo_producto = RepositorioProductoSQL()

# Inyectamos los repos al caso de uso
crear_orden_use_case = CrearOrdenUseCase(repo_orden, repo_cliente)
crear_producto_use_case = CrearProductoUseCase(repo_producto)
crear_cliente_use_case = CrearClienteUseCase(repo_cliente)

eliminar_cliente_uc = EliminarClienteUseCase(repo_cliente)
eliminar_producto_uc = EliminarProductoUseCase(repo_producto)
eliminar_orden_uc = EliminarOrdenUseCase(repo_orden)

obtener_orden_use_case = ObtenerOrdenUseCase(repo_orden)
obtener_cliente_use_case = ObtenerClienteUseCase(repo_cliente)
obtener_producto_use_case = ObtenerProductoUseCase(repo_producto)


@app.post("/ordenes")
def crear_orden_endpoint(orden_dto: OrdenCreateDTO):
    try:
        items_dominio = [
            ItemOrden(i.producto_id, i.cantidad, i.precio_unitario) 
            for i in orden_dto.items
        ]
        
        nueva_orden = Orden(
            id=0,
            cliente_id=orden_dto.cliente_id,
            items=items_dominio
        )

        # Invocamos al Caso de Uso
        orden_creada = crear_orden_use_case.ejecutar(nueva_orden)

        # Respondemos
        return {"mensaje": "Orden creada", "id": orden_creada.id, "total": orden_creada.total}

    except ErrorValidacionOrden as e:
        # Errores de negocio -> 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Errores inesperados -> 500 Internal Server Error
        print(f"Error interno: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    

@app.post("/productos", response_model=ProductoResponseDTO)
def crear_producto(dto: ProductoCreateDTO):
    # Mapeo DTO -> Entidad
    nuevo_prod = Producto(id=0, descripcion=dto.descripcion, precio_actual=dto.precio_actual)
    return crear_producto_use_case.ejecutar(nuevo_prod)

@app.post("/clientes", response_model=ClienteResponseDTO)
def crear_cliente(dto: ClienteCreateDTO):
    # Mapeo DTO -> Entidad
    nuevo_cliente = Cliente(id=0, nombre=dto.nombre, activo=dto.activo)
    return crear_cliente_use_case.ejecutar(nuevo_cliente)

#=====================================================
#GETS

@app.get("/ordenes/obtener", response_model=OrdenResponseDTO)
def obtener_orden_endpoint(id_orden: int):
    orden = obtener_orden_use_case.ejecutar(id_orden)
    
    if orden is None:
        raise HTTPException(status_code=404, detail=f"Orden {id_orden} no encontrada")
        
    return orden

@app.get("/clientes/obtener", response_model=ClienteResponseDTO)
def obtener_cliente(id_cliente: int):
    cliente = obtener_cliente_use_case.ejecutar(id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.get("/productos/obtener", response_model=ProductoResponseDTO)
def obtener_producto(id_producto: int):
    producto = obtener_producto_use_case.ejecutar(id_producto)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

#=====================================================
#DELETES

@app.delete("/ordenes/borrar")
def eliminar_orden_endpoint(id_orden: int):
    exito = eliminar_orden_uc.ejecutar(id_orden)
    if not exito:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return {"mensaje": "Orden eliminada con éxito"}

@app.delete("/clientes/borrar")
def eliminar_cliente_endpoint(id_cliente: int):
    exito = eliminar_cliente_uc.ejecutar(id_cliente)
    if not exito:
        raise HTTPException(
            status_code=400, 
            detail="No se pudo eliminar: El cliente no existe O tiene órdenes asociadas."
        )
    return {"mensaje": "Cliente eliminado con éxito"}

@app.delete("/productos/borrar")
def eliminar_producto_endpoint(id_producto: int):
    exito = eliminar_producto_uc.ejecutar(id_producto)
    if not exito:
        raise HTTPException(
            status_code=400, 
            detail="No se pudo eliminar: El producto no existe O está presente en órdenes."
        )
    return {"mensaje": "Producto eliminado con éxito"}