from app.domain.order import Order

class CreateOrderUseCase:
    def execute(self, customer_id: int) -> Order:
        order = Order(customer_id=customer_id, items={})

        return order