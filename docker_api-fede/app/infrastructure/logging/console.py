from app.domain.interfaces.logger import LoggerInterface

class ConsoleLogger(LoggerInterface):
    def log_info(self, message: str) -> None:
        # Implementación concreta: Salida a consola
        print(f"[LOGGER PROVIDER]: {message}")