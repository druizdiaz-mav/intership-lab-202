from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.domain.entities import Persona, EstadoPersona

class CustomerRepositoryInMemory(CustomerRepositoryInterface):
    def get_by_id(self, id_cliente: int) -> Persona | None:
        for persona in lista_personas:
            if persona.id == id_cliente:
                return persona
        return None

