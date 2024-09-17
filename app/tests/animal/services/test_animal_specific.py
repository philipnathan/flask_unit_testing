import pytest
from unittest.mock import MagicMock

from app.animal.services.SpecificAnimalServices import SpecificAnimalServices


@pytest.fixture
def animal_service():
    repository = MagicMock()
    return SpecificAnimalServices(repository)


@pytest.fixture
def mock_return():
    return {
        1: {
            "animal_id": 1,
            "species": "Dog",
            "age": 3,
            "gender": "Male",
            "special_requirements": "Needs regular exercise",
        },
    }


def test_get_specific(animal_service, mock_return):
    # arrange
    animal_service.repository.get_by_id.return_value = mock_return

    # act
    result = animal_service.get_specific_animals(1)

    # assert
    animal_service.repository.get_by_id.assert_called_once_with(1)
    assert result == mock_return


def test_delete_specific(animal_service):
    # arrange
    animal_service.repository.delete_specific.return_value = None

    # act
    result = animal_service.delete_specific_animal(1)

    # assert
    animal_service.repository.delete_specific.assert_called_once_with(1)
    assert result is None


def test_edit_specific(animal_service):
    # arrange
    mock_get = {
        "animal_id": 2,
        "species": "Dog",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    mock_return = {
        "animal_id": 2,
        "species": "Cat",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    animal_service.repository.get_by_id.return_value = mock_get
    animal_service.repository.edit_specific.return_value = mock_return

    # act
    result = animal_service.edit_specific_animal(2, {"species": "Cat"})

    # assert
    animal_service.repository.get_by_id.assert_called_once_with(2)
    assert result == mock_return


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ([], ValueError),
        ({}, ValueError),
        (
            {
                "animal_id": 2,
                "species": "Cat",
                "age": 3,
                "gender": "Male",
                "special_requirements": "Needs regular exercise",
            },
            ValueError,
        ),
        ({"spec": ""}, ValueError),
        ({"species": ""}, ValueError),
        ({"species": 123}, ValueError),
        ({"age": "umur"}, ValueError),
        ({"species": -1}, ValueError),
        ({"gender": 123}, ValueError),
        ({"gender": "fimel"}, ValueError),
    ],
)
def test_edit_specific_logic(animal_service, mock_input, expected):
    # arrage
    mock_get = {
        "animal_id": 2,
        "species": "Dog",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    animal_service.repository.get_by_id.return_value = mock_get

    with pytest.raises(expected):
        animal_service.edit_specific_animal(2, mock_input)
