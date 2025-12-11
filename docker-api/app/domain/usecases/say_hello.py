from app.domain.interfaces.logger_interface import LoggerInterface

class SayHelloUseCase:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def execute(self):
        mensaje = "Hello, World!"
        self.logger.log(mensaje)
        return mensaje

