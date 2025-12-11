from app.domain.interfaces.logger_interface import LoggerInterface

class SayHelloUseCase:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def execute(self) -> str:
        message = "Hola"
        self.logger.log(message)  # logea la respuesta
        return message