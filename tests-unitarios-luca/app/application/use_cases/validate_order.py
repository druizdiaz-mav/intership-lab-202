from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.entities import Orden, LineaDeOrden
from app.domain.exceptions import InvalidOrderException

class ValidateOrderUseCase:
    def __init__(self, customer_repository: CustomerRepositoryInterface, item_repository: ItemRepositoryInterface, exception_to_raise):
        self.customer_repository = customer_repository
        self.item_repository = item_repository
        self.exception_to_raise = exception_to_raise  #Es correcto? No estoy seguro si es conveniente inyectar la excepción ya que se utiliza para hacer el raise simplemente, quizas es conveniente inyectar un logger con los errores

    def execute(self, orden: Orden) -> float:

        #Valido cantidad de items
        if len(orden.lineas_de_orden) == 0:
            raise self.exception_to_raise("La orden no tiene productos.")

        #Valido cliente
        customer = self.customer_repository.get_by_id(orden.id_persona)
        if not customer or not customer.is_active():
            raise self.exception_to_raise("El cliente no es activo.")

        #Validación de Items y Cálculo de Total 
        total_calculado = self._procesar_items(orden, self.exception_to_raise)

        # Validación de Total Global
        if total_calculado > 10000:
             raise self.exception_to_raise("El total de la orden excede el límite permitido.")

        #Retorno total calculado
        return total_calculado

    def _procesar_items(self, orden: Orden, exception_to_raise) -> float:
        for linea in orden.lineas_de_orden:
            precio_real = self.item_repository.get_price(linea.id_producto)
            
            if precio_real is None:
                raise exception_to_raise(f"Producto {linea.id_producto} no existe.")
            
            # Asignamos el precio a la entidad
            linea.precio_unitario = precio_real

        #El use case pide total a la entidad Orden
        total_calculado = orden.calcular_total(exception_to_raise)

        return total_calculado