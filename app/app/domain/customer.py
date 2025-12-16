class Customer:
    def __init__(self, customer_id: int, name: str, active: bool = True):
        self.id = customer_id
        self.name = name
        self.active = active

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def is_active(self) -> bool:
        return self.active