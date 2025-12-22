from app.application.interfaces.product_repository_interface import ProductRepositoryInterface
from app.domain.entities import Producto
from app.infrastructure.database import get_connection

class ProductRepository(ProductRepositoryInterface):

    def create(self, producto: Producto) -> Producto:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO productos (nombre, precio) VALUES (%s, %s) RETURNING id",
            (producto.nombre, producto.precio)
        )
        producto.id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return producto

    def get_by_id(self, product_id: int) -> Producto | None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, nombre, precio FROM productos WHERE id = %s",
            (product_id,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return None

        return Producto(*row)

    def delete(self, product_id: int) -> None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM productos WHERE id = %s", (product_id,))
        conn.commit()
        cur.close()
        conn.close()
