import pytest

from app.application.usecases.get_customer_by_id import GetCustomerByIdUseCase
from app.infrastructure.repositories.customer_repository import MockCustomerRepository

def test_get_customer_by_id_usecase():
    customer_repository = MockCustomerRepository()
    get_customer_by_id_usecase = GetCustomerByIdUseCase(customer_repository)

    # Test valid customer ID
    customer = get_customer_by_id_usecase.execute(customer_id=1)

    assert customer.get_id() == 1
    assert customer.get_name() == "Mock Customer 1"
    assert customer.is_active() is True

    # Test invalid customer ID
    with pytest.raises(Exception) as exc_info:
        get_customer_by_id_usecase.execute(customer_id=150)

    assert str(exc_info.value) == "Customer not found"