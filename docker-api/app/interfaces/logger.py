from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass