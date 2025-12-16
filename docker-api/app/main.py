from fastapi import FastAPI

from app.usecases.hello import GetGreetingUseCase
from app.framework.console_logger import ConsoleLogger
from app.interfaces.routers import create_hello_router

def create_application() -> FastAPI:
    app = FastAPI()

    hello_use_case = GetGreetingUseCase(ConsoleLogger())
    hello_router = create_hello_router(hello_use_case)

    app.include_router(hello_router)

    return app

app = create_application()