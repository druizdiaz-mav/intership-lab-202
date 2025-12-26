from app.domain.order import Order

class OrderRemoveItemUseCase:
    def __init__(self, order: Order):
        self.order = order

    def execute(self, item_id: int, qty: int = 0) -> Order:
        self.order.remove_item(item_id=item_id, qty=qty)

        return self.order