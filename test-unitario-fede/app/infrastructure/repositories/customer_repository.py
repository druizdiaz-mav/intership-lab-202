import psycopg2
from typing import Optional
from app.domain.entities import Cliente
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface
from app.infrastructure.connect_db import get_db_connection

class RepositorioClienteSQL(RepositorioClienteInterface):
    
    def obtener_por_id(self, id_cliente: int) -> Optional[Cliente]:
        conn = None
        try:
            # Abrimos conexión
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Query SQL para evitar acciones peligrosas
            query = "SELECT id, nombre, activo FROM clientes WHERE id = %s" #%s como marcador de posición para el ID
            cursor.execute(query, (id_cliente,)) 
            
            # Obtenemos el resultado
            row = cursor.fetchone()
            
            # Si no hay datos, devolvemos None
            if row is None:
                return None
            
            # Transformamos la tupla SQL en objeto cliente
            cliente = Cliente(id=row[0], nombre=row[1], activo=row[2])
            
            return cliente

        except Exception as e:
            print(f"Error en RepositorioClienteSQL: {e}")
            return None
            
        finally:
            # Cerramos la conexión para no saturar la base
            if conn:
                cursor.close()
                conn.close()
                
    def guardar(self, cliente: Cliente) -> Cliente:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            # Insertamos y pedimos el ID generado
            query = "INSERT INTO clientes (nombre, activo) VALUES (%s, %s) RETURNING id"
            cursor.execute(query, (cliente.nombre, cliente.activo))
            
            nuevo_id = cursor.fetchone()[0]
            conn.commit()
            
            cliente.id = nuevo_id
            return cliente
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    def eliminar(self, id_cliente: int) -> bool:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(query, (id_cliente,))
            
            filas_borradas = cursor.rowcount
            conn.commit()
            return filas_borradas > 0

        except psycopg2.errors.ForeignKeyViolation:
            conn.rollback()
            print(f"BLOQUEO: El cliente {id_cliente} tiene órdenes asociadas.")
            return False

        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()
            conn.close()