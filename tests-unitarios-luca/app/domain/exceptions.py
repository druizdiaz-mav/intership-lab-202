class InvalidOrderException(Exception):
    #Excepciones personalizadas para la validación de las reglas de negocios en las órdenes (archivo que quedó viejo de la anterior actividad)
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

