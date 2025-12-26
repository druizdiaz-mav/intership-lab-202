from fastapi import FastAPI, HTTPException
from datetime import datetime

from app.infrastructure.repositories.product_repository import ProductRepository
from app.infrastructure.repositories.customer_repository import CustomerRepository
from app.infrastructure.repositories.order_repository import OrderRepository

from app.application.useCases.create_product import CreateProduct
from app.application.useCases.get_product import GetProduct
from app.application.useCases.delete_product import DeleteProduct

from app.application.useCases.create_customer import CreateCustomer
from app.application.useCases.get_customer import GetCustomer
from app.application.useCases.delete_customer import DeleteCustomer

from app.application.useCases.create_order import CreateOrder
from app.application.useCases.get_order import GetOrder
from app.application.useCases.delete_order import DeleteOrder

from app.domain.entities import Orden, ItemOrden

app = FastAPI()

product_repo = ProductRepository()
customer_repo = CustomerRepository()
order_repo = OrderRepository()

@app.post("/productos")
def crear_producto(nombre: str, precio: float):
    use_case = CreateProduct(product_repo)
    return use_case.execute(nombre, precio)

@app.get("/productos/{product_id}")
def obtener_producto(product_id: int):
    use_case = GetProduct(product_repo)
    producto = use_case.execute(product_id)
    if not producto:
        raise HTTPException(status_code=404)
    return producto

@app.delete("/productos/{product_id}")
def eliminar_producto(product_id: int):
    use_case = DeleteProduct(product_repo)
    use_case.execute(product_id)
    return {"status": "deleted"}

@app.post("/clientes")
def crear_cliente(nombre: str, activo: bool):
    use_case = CreateCustomer(customer_repo)
    return use_case.execute(nombre, activo)

@app.get("/clientes/{customer_id}")
def obtener_cliente(customer_id: int):
    use_case = GetCustomer(customer_repo)
    cliente = use_case.execute(customer_id)
    if not cliente:
        raise HTTPException(status_code=404)
    return cliente

@app.delete("/clientes/{customer_id}")
def eliminar_cliente(customer_id: int):
    use_case = DeleteCustomer(customer_repo)
    use_case.execute(customer_id)
    return {"status": "deleted"}

@app.post("/ordenes")
def crear_orden(cliente_id: int, items: list[dict]):
    items_orden = [
        ItemOrden(
            producto_id=item["producto_id"],
            cantidad=item["cantidad"],
            precio_unitario=item["precio_unitario"]
        )
        for item in items
    ]

    total = sum(
        item.cantidad * item.precio_unitario
        for item in items_orden
    )

    orden = Orden(
        id=None,
        cliente_id=cliente_id,
        fecha=datetime.utcnow(),
        total=total,
        items=items_orden
    )

    use_case = CreateOrder(order_repo, customer_repo)
    return use_case.execute(orden)

@app.get("/ordenes/{order_id}")
def obtener_orden(order_id: int):
    use_case = GetOrder(order_repo)
    orden = use_case.execute(order_id)
    if not orden:
        raise HTTPException(status_code=404)
    return orden

@app.delete("/ordenes/{order_id}")
def eliminar_orden(order_id: int):
    use_case = DeleteOrder(order_repo)
    use_case.execute(order_id)
    return {"status": "deleted"}
