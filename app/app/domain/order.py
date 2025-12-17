from app.domain.customer import Customer
from app.domain.item import Item

class Order:
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        self.items = dict()

    def add_item(self, item_id: int, qty: int):
        self.items[item_id] = qty

    def remove_item(self, item_id: int, qty: int = 0):
        if item_id in self.items:
            if (qty == 0):
                del self.items[item_id]
                return

            self.items[item_id] -= qty

            if self.items[item_id] <= 0:
                del self.items[item_id]