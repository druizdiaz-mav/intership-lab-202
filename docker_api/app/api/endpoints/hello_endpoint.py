from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.domain.usecases.say_hello import SayHelloUseCase
from app.infrastructure.logger.console_logger import ConsoleLogger

router = APIRouter()

# Crear logger e inyectarlo en el use case
logger = ConsoleLogger()
usecase = SayHelloUseCase(logger)

@router.get("/hello", response_class=PlainTextResponse, status_code=200)
def read_hello():
    return usecase.execute()