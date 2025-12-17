from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.entities import Orden
from app.domain.exceptions import InvalidOrderException

class ValidateOrderUseCase:
    def __init__(self, customer_repository: CustomerRepositoryInterface, item_repository: ItemRepositoryInterface):
        self.customer_repository = customer_repository
        self.item_repository = item_repository

    def execute(self, orden):

        #Valido cantidad de items
        if len(orden.lineas_de_orden) == 0:
            raise InvalidOrderException("La orden no tiene productos.")

        #Valido cliente
        if not self.customer_repository.is_active(orden.id_persona):
            raise InvalidOrderException("El cliente no es activo.")

        #Validación de Items y Cálculo de Total 
        total_calculado = self._procesar_items(orden.lineas_de_orden)

        # Validación de Total Global
        if total_calculado > 10000:
             raise InvalidOrderException("El total de la orden excede el límite permitido.")

        #Retorno total calculado
        return total_calculado
        
    def _procesar_items(self, items) -> float:
        total = 0.0
        
        for linea in items:
            # Validar cantidad
            if linea.cantidad <= 0:
                raise InvalidOrderException(f"La cantidad del producto ID {linea.id_producto} es inválida.")

            # Obtener precio
            precio = self.item_repository.get_price(linea.id_producto)
            
            # Validar precio
            if precio is None: 
                raise InvalidOrderException(f"El producto ID {linea.id_producto} no existe.")
            if precio <= 0:
                raise InvalidOrderException(f"El producto ID {linea.id_producto} tiene precio inválido.")

            # Acumular en total
            total += precio * linea.cantidad
        
        return total