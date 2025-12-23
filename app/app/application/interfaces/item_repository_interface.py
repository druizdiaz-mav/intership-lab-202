from app.domain.item import Item
from abc import ABC, abstractmethod

class ItemRepositoryInterface(ABC):
    @abstractmethod
    def get_item_by_id(self, item_id: int) -> Item:
        """Retrieve an item by its ID."""
        pass