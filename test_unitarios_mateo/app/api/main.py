from fastapi import FastAPI, HTTPException
from app.infrastructure.repositories.product_repository import ProductRepository
from app.application.useCases.create_product import CreateProduct
from app.application.useCases.get_product import GetProduct
from app.application.useCases.delete_product import DeleteProduct

app = FastAPI()

repo = ProductRepository()

@app.post("/productos")
def crear_producto(nombre: str, precio: float):
    use_case = CreateProduct(repo)
    return use_case.execute(nombre, precio)

@app.get("/productos/{product_id}")
def obtener_producto(product_id: int):
    use_case = GetProduct(repo)
    producto = use_case.execute(product_id)
    if not producto:
        raise HTTPException(status_code=404)
    return producto

@app.delete("/productos/{product_id}")
def eliminar_producto(product_id: int):
    use_case = DeleteProduct(repo)
    use_case.execute(product_id)
    return {"status": "deleted"}
