from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.application.interfaces.item_repository_interface import ItemRepositoryInterface
from app.domain.exception import DomainException
from app.domain.customer import Customer
from app.domain.order import Order
from app.domain.item import Item

class ValidateOrderUseCase:
    def __init__(self, customer_repository: CustomerRepositoryInterface, item_repository: ItemRepositoryInterface):
        self.customer_repository = customer_repository
        self.item_repository = item_repository

    def execute(self, order: Order) -> bool:
        customer = self.customer_repository.get_customer_by_id(order.customer_id)

        if (not customer.is_active()):
            raise DomainException("The customer is not active")

        if (len(order.items) == 0):
            raise DomainException("The order must have at least one item")

        total = 0.0

        for order_item in order.items:
            item_id = order_item.item_id
            qty = order_item.quantity

            item = self.item_repository.get_item_by_id(item_id)
            
            if (qty <= 0):
                raise DomainException("The item quantity must be greater than zero")

            if (item.get_price() <= 0):
                raise DomainException("The item price must be greater than zero")

            total += item.get_price() * qty

        if (total > 10000.0):
            raise DomainException("The total amount of the order must not exceed $10,000.00")

        return True