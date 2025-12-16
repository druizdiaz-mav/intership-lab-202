class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

class Order:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = items