import psycopg2
from typing import Optional
from app.domain.entities import Producto
from app.application.interfaces.product_repository_interface import RepositorioProductoInterface
from app.infrastructure.connect_db import get_db_connection

class RepositorioProductoSQL(RepositorioProductoInterface):
    
    def obtener_por_id(self, id_producto: int) -> Optional[Producto]:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT id, nombre, precio FROM productos WHERE id = %s" #%s como marcador de posición para el ID
            cursor.execute(query, (id_producto,))
            row = cursor.fetchone()
            
            if row:
                return Producto(id=row[0], descripcion=row[1], precio_actual=float(row[2]))
            return None
        finally:
            cursor.close()
            conn.close()

    def guardar(self, producto: Producto) -> Producto:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            #Insertamos y pedimos que nos devuelva el ID autogenerado
            query = """
                INSERT INTO productos (nombre, precio) 
                VALUES (%s, %s) RETURNING id
            """
            cursor.execute(query, (producto.descripcion, producto.precio_actual))
            
            # Obtenemos el ID nuevo
            nuevo_id = cursor.fetchone()[0]
            conn.commit()
            
            # Actualizamos el objeto con su nuevo ID
            producto.id = nuevo_id
            return producto
            
        except Exception as e:
            conn.rollback() # Si falla, deshacemos todo
            raise e
        finally:
            cursor.close()
            conn.close()


    def eliminar(self, id_producto: int) -> bool:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = "DELETE FROM productos WHERE id = %s"
            cursor.execute(query, (id_producto,))
            
            filas_borradas = cursor.rowcount
            conn.commit()
            return filas_borradas > 0

        except psycopg2.errors.ForeignKeyViolation:
            conn.rollback()
            print(f"BLOQUEO: El producto {id_producto} está en órdenes existentes.")
            return False

        except Exception as e:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()