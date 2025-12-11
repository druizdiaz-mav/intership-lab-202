from app.domain.greeting import Greeting
from app.interfaces.logger import LoggerInterface

class GetGreetingUseCase:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def execute(self) -> Greeting:
        # business rule: produce greeting entity
        greeting = Greeting("Hola")

        self.logger.log(greeting.get_message())

        return greeting