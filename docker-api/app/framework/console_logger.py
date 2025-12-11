import logging

from app.interfaces.logger import LoggerInterface

class ConsoleLogger(LoggerInterface):
    def __init__(self) -> None:
        self._logger = logging.getLogger("app")
        self._logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        self._logger.addHandler(handler)

    def log(self, message: str) -> None:
        self._logger.info(message)