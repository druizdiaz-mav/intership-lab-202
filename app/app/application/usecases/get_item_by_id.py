from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.item import Item

class GetItemByIdUseCase():
    def __init__(self, item_repository: ItemRepositoryInterface):
        self.item_repository = item_repository

    def execute(self, item_id: int) -> Item:
        return self.item_repository.get_item_by_id(item_id)