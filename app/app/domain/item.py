class Item:
    def __init__(self, item_id: int, description: str, price: float):
        self.id = item_id
        self.description = description
        self.price = price

    def get_id(self) -> int:
        return self.id

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price