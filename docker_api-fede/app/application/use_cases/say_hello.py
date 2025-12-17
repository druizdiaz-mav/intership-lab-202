from app.domain.interfaces.logger import LoggerInterface

class SayHelloUseCase:
    def __init__(self, logger: LoggerInterface):
        # Inyección de Dependencia: El logger viene de afuera
        self.logger = logger

    def execute(self) -> dict:
        response = {"message": "Hello World from Clean Architecture"}
        
        # Usamos el contrato del logger
        self.logger.log_info(f"Case executed successfully. Response: {response}")
        
        return response