from fastapi import APIRouter, Depends
from app.domain.interfaces.logger import LoggerInterface
from app.infrastructure.logging.console import ConsoleLogger
from app.application.use_cases.say_hello import SayHelloUseCase

router = APIRouter()

# Provider: Fabrica la implementación del Logger
def get_logger_provider() -> LoggerInterface:
    return ConsoleLogger()

# Provider: Fabrica el Caso de Uso e inyecta el Logger
def get_say_hello_use_case(
    logger: LoggerInterface = Depends(get_logger_provider)
) -> SayHelloUseCase:
    return SayHelloUseCase(logger)

# Endpoint: Recibe el Caso de Uso listo para usar
@router.get("/hello")
def hello_endpoint(
    use_case: SayHelloUseCase = Depends(get_say_hello_use_case)
):
    return use_case.execute()