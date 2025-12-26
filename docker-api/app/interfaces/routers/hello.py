from fastapi import APIRouter
from app.usecases.hello import GetGreetingUseCase

def create_hello_router(usecase: GetGreetingUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/hello")
    def hello():
        greeting = usecase.execute()

        return greeting.get_message()

    return router