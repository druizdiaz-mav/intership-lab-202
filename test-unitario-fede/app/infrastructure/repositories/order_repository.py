from typing import Optional
from app.domain.entities import Orden, ItemOrden
from app.infrastructure.connect_db import get_db_connection
from app.application.interfaces.orden_repository_interface import RepositorioOrdenInterface

class RepositorioOrdenSQL(RepositorioOrdenInterface):
    
    def guardar(self, orden: Orden) -> Orden:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            # Insertamos órden
            query_orden = """
                INSERT INTO ordenes (cliente_id, total, fecha) 
                VALUES (%s, %s, %s) RETURNING id
            """
            cursor.execute(query_orden, (orden.cliente_id, orden.total, orden.fecha))
            orden_id_generado = cursor.fetchone()[0]
            
            # Insertamos los Ítems
            query_item = """
                INSERT INTO items_orden (orden_id, producto_id, cantidad, precio_unitario) 
                VALUES (%s, %s, %s, %s)
            """
            
            for item in orden.items:
                cursor.execute(query_item, (
                    orden_id_generado, 
                    item.producto_id, 
                    item.cantidad, 
                    item.precio_unitario
                ))
            
            conn.commit()
            
            orden.id = orden_id_generado
            return orden

        except Exception as e:
            # Si algo falla, borramos todo
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
            
    def obtener_por_id(self, id_orden: int) -> Optional[Orden]:
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                # Buscamos la orden
                query_orden = "SELECT id, cliente_id, fecha, total FROM ordenes WHERE id = %s"
                cursor.execute(query_orden, (id_orden,))
                row_orden = cursor.fetchone()

                # Si no existe la orden, paramos
                if row_orden is None:
                    return None

                # Buscamos los items
                query_items = """
                    SELECT producto_id, cantidad, precio_unitario 
                    FROM items_orden 
                    WHERE orden_id = %s
                """
                cursor.execute(query_items, (id_orden,))
                rows_items = cursor.fetchall() 

                lista_items = []
                for item in rows_items:
                    objeto_item = ItemOrden(
                        producto_id=item[0], 
                        cantidad=item[1], 
                        precio_unitario=float(item[2])
                    )
                    lista_items.append(objeto_item)

                # Armamos la órden final
                orden_encontrada = Orden(
                    id=row_orden[0],
                    cliente_id=row_orden[1],
                    fecha=row_orden[2],
                    total=float(row_orden[3]),
                    items=lista_items
                )

                return orden_encontrada

            except Exception as e:
                print(f"Error obteniendo orden: {e}")
                return None

            finally:
                cursor.close()
                conn.close()


    def eliminar(self, id_orden: int) -> bool:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            #Borramos primero los ítems de la Órden
            query_items = "DELETE FROM items_orden WHERE orden_id = %s"
            cursor.execute(query_items, (id_orden,))

            #Borramos la orden
            query_orden = "DELETE FROM ordenes WHERE id = %s"
            cursor.execute(query_orden, (id_orden,))
            
            filas_borradas = cursor.rowcount
            conn.commit()
            
            # Si borró la cabecera, devolvemos True
            return filas_borradas > 0

        except Exception as e:
            conn.rollback()
            print(f"Error eliminando orden: {e}")
            return False
        finally:
            cursor.close()
            conn.close()