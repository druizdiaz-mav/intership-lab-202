from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass