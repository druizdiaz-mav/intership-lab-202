class InvalidOrderException(Exception):
    #Excepciones personalizadas para la validación de las reglas de negocios en las órdenes
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

