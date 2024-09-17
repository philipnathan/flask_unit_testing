from unittest.mock import MagicMock
import pytest

from app.animal.services.AllAnimalServices import AllAnimalServices


@pytest.fixture
def animal_service():
    repository = MagicMock()
    return AllAnimalServices(repository)


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
        2: {
            "animal_id": 2,
            "species": "Cat",
            "age": 2,
            "gender": "Female",
            "special_requirements": "Indoor cat, needs litter box",
        },
    }


def test_get_all_animal(animal_service, mock_return):
    # arrage
    animal_service.repository.get_all.return_value = mock_return

    # act
    result = animal_service.get_all_animal()

    # assert
    animal_service.repository.get_all.assert_called_once_with()
    assert result == mock_return


def test_add_animal(animal_service):
    # arrange
    mock_return = {
        "animal_id": 3,
        "species": "Cat",
        "age": 2,
        "gender": "Female",
        "special_requirements": "Indoor cat, needs litter box",
    }

    animal_service.repository.add_new.return_value = mock_return

    # act
    mock_json = {
        "species": "Cat",
        "age": 2,
        "gender": "Female",
        "special_requirements": "Indoor cat, needs litter box",
    }
    result = animal_service.add_animal(mock_json)

    # assert
    animal_service.repository.add_new.assert_called_once_with(**mock_json)
    assert result == mock_return


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (
            {
                "test": "test",
                "age": 3,
                "gender": "Male",
                "special_requirements": "Needs regular exercise",
            },
            ValueError,
        ),
        (
            {
                "age": 2,
                "gender": "Female",
                "special_requirements": "Indoor cat, needs litter box",
            },
            ValueError,
        ),
        (
            {
                "species": 123,
                "age": 2,
                "gender": "Female",
                "special_requirements": "Indoor cat, needs litter box",
            },
            ValueError,
        ),
        (
            {
                "species": "Cat",
                "age": -1,
                "gender": "Female",
                "special_requirements": "Indoor cat, needs litter box",
            },
            ValueError,
        ),
        (
            {
                "species": "Cat",
                "age": 2,
                "gender": "Upin",
                "special_requirements": "Indoor cat, needs litter box",
            },
            ValueError,
        ),
    ],
)
def test_add_animal_checker(animal_service, mock_input, expected):
    with pytest.raises(expected):
        animal_service.add_animal_checker(mock_input)
