from app.domain.order import Order

class CreateOrderUseCase:
    def execute(self, customer_id: int) -> Order:
        order = Order(order_id=0, customer_id=customer_id, total=0.0)

        return order