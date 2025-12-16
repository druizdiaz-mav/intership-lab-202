from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.item import Item

class MockItemRepository(ItemRepositoryInterface):
    def get_item_by_id(self, item_id: int) -> Item:
        if (item_id > 100):
            raise Exception("Item not found")

        return Item(item_id=item_id, description=f"Mock Item {item_id}", price=item_id * 1.0)