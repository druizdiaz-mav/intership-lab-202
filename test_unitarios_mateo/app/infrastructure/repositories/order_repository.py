from app.application.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)
from app.domain.entities import Orden, ItemOrden
from app.infrastructure.database import get_connection

class OrderRepository(OrderRepositoryInterface):

    def create(self, orden: Orden) -> Orden:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO ordenes (cliente_id, fecha, total)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (orden.cliente_id, orden.fecha, orden.total)
        )
        orden.id = cur.fetchone()[0]
        
        for item in orden.items:
            cur.execute(
                """
                INSERT INTO items_orden
                (orden_id, producto_id, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    orden.id,
                    item.producto_id,
                    item.cantidad,
                    item.precio_unitario
                )
            )

        conn.commit()
        cur.close()
        conn.close()
        return orden

    def get_by_id(self, order_id: int) -> Orden | None:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT id, cliente_id, fecha, total FROM ordenes WHERE id = %s",
            (order_id,)
        )
        orden_row = cur.fetchone()

        if not orden_row:
            cur.close()
            conn.close()
            return None

        cur.execute(
            """
            SELECT producto_id, cantidad, precio_unitario
            FROM items_orden
            WHERE orden_id = %s
            """,
            (order_id,)
        )

        items_rows = cur.fetchall()
        cur.close()
        conn.close()

        items = [
            ItemOrden(
                producto_id=row[0],
                cantidad=row[1],
                precio_unitario=row[2]
            )
            for row in items_rows
        ]

        return Orden(
            id=orden_row[0],
            cliente_id=orden_row[1],
            fecha=orden_row[2],
            total=orden_row[3],
            items=items
        )

    def delete(self, order_id: int) -> None:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM items_orden WHERE orden_id = %s",
            (order_id,)
        )
        cur.execute(
            "DELETE FROM ordenes WHERE id = %s",
            (order_id,)
        )

        conn.commit()
        cur.close()
        conn.close()
