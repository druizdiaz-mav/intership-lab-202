from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.exception import DomainException
from app.domain.order import Order
from app.domain.item import Item

class CalculateOrderTotalUseCase:
    def __init__(self, item_repository: ItemRepositoryInterface):
        self.item_repository = item_repository

    def execute(self, order: Order) -> Order:
        for order_item in order.items:
            item_id = order_item.item_id
            qty = order_item.quantity

            item = self.item_repository.get_item_by_id(item_id)

            order.total += item.get_price() * qty

        return order