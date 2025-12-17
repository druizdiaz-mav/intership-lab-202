from fastapi import APIRouter, Depends
from app.domain.usecases.say_hello import SayHelloUseCase
from app.infraestructure.logger.console_logger import ConsoleLogger

router = APIRouter()

def get_logger():
    return ConsoleLogger()

def get_use_case(logger = Depends(get_logger)):
    return SayHelloUseCase(logger)

@router.get("/hello")
def say_hello(use_case: SayHelloUseCase = Depends(get_use_case)):
    return {"response" : use_case.execute()}