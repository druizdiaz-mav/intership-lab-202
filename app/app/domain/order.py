from app.domain.customer import Customer
from app.domain.item import Item

class OrderItem:
    def __init__(self, item_id: int, quantity: int):
        self.item_id = item_id
        self.quantity = quantity

class Order:
    def __init__(self, order_id: int, customer_id: int, total: float):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = list()
        self.total = total

    def add_item(self, item_id: int, qty: int):
        self.items.append(OrderItem(item_id, qty))

    def remove_item(self, item_id: int, qty: int = 0):
        if item_id in self.items:
            if (qty == 0):
                del self.items[item_id]
                return

            self.items[item_id] -= qty

            if self.items[item_id] <= 0:
                del self.items[item_id]

    def get_items(self) -> list[OrderItem]:
        return self.items

    def get_total(self) -> float:
        return self.total

    def get_customer_id(self) -> int:
        return self.customer_id

    def get_order_id(self) -> int:
        return self.order_id