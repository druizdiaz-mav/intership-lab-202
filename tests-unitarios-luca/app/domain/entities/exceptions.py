class DomainException(Exception):
    """Base para todos los errores de negocio o para excepciones basicas de dominio"""
    pass

class EntityNotFound(DomainException):
    """Entidad no encontrada"""
    pass

class BusinessRuleValidation(DomainException):
    """Falla regla de negocio"""
    pass