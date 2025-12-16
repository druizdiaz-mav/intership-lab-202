from app.domain.order import Order

class OrderAddItemUseCase:
    def __init__(self, order: Order):
        self.order = order

    def execute(self, item_id: int, qty: int) -> Order:
        self.order.add_item(item_id=item_id, qty=qty)

        return self.order