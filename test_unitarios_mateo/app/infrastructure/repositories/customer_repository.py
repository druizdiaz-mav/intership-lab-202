from app.application.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface
)
from app.domain.entities import Cliente
from app.infrastructure.database import get_connection

class CustomerRepository(CustomerRepositoryInterface):

    def create(self, cliente: Cliente) -> Cliente:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO clientes (nombre, activo)
            VALUES (%s, %s)
            RETURNING id
            """,
            (cliente.nombre, cliente.activo)
        )
        cliente.id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return cliente

    def get_by_id(self, customer_id: int) -> Cliente | None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, nombre, activo FROM clientes WHERE id = %s",
            (customer_id,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return None

        return Cliente(*row)

    def delete(self, customer_id: int) -> None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM clientes WHERE id = %s",
            (customer_id,)
        )
        conn.commit()
        cur.close()
        conn.close()
