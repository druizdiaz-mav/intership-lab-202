from app.application.interfaces.orden_repository_interface import RepositorioOrdenInterface

class EliminarOrdenUseCase:
    def __init__(self, repo: RepositorioOrdenInterface):
        self.repo = repo

    def ejecutar(self, id_orden: int) -> bool:
        return self.repo.eliminar(id_orden)