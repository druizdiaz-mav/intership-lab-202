import pytest

from app.application.usecases.get_item_by_id import GetItemByIdUseCase
from app.infrastructure.repositories.mock_item_repository import MockItemRepository

def test_get_item_by_id_usecase():
    item_repository = MockItemRepository()
    get_item_by_id_usecase = GetItemByIdUseCase(item_repository)

    # Test valid customer ID
    item = get_item_by_id_usecase.execute(item_id=11)

    assert item.get_id() == 11
    assert item.get_description() == "Mock Item 11"
    assert item.get_price() == 11.0

    # Test invalid customer ID
    with pytest.raises(Exception) as exc_info:
        get_item_by_id_usecase.execute(item_id=150)

    assert str(exc_info.value) == "Item not found"