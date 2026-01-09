from app.domain.interfaces.logger_interface import LoggerInterface

class ConsoleLogger(LoggerInterface):
    def log(self, message: str) -> None:
        print(message)