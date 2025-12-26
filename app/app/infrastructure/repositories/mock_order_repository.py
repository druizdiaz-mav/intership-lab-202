from app.application.interfaces.order_repository_interface import OrderRepositoryInterface
from app.domain.order import Order

class MockOrderRepository(OrderRepositoryInterface):
    def get_order_by_id(self, order_id: int) -> Order:
        if (order_id > 100):
            raise Exception("Order not found")

        order = Order(
            order_id=order_id,
            name=f"Mock Order {order_id}",
            active=order_id % 2 == 1
        )

        return order

    def add_order(self, order: Order) -> Order:
        return order

    def remove_order(self, order_id: int):
        return
