from unittest.mock import patch
import pytest

from app.animal.repositories.AnimalRepository import AnimalRepository


@pytest.fixture
def mock_db():
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


@pytest.fixture
def repository(mock_db):
    with patch("app.animal.repositories.AnimalRepository.animal_sample", mock_db):
        yield AnimalRepository()


def test_get_all(repository, mock_db):
    # act
    result = repository.get_all()

    # assert
    assert result == mock_db


def test_get_specific_succeed(repository, mock_db):
    # act
    result = repository.get_by_id(1)

    # assert
    assert result == mock_db[1]


def test_get_specific_failed(repository):
    # act
    with pytest.raises(ValueError) as e:
        repository.get_by_id(1000000)

    # assert
    assert str(e.value) == "Animal with ID 1000000 is not exist."


def test_delete_specific_succeed(repository, mock_db):
    # act
    result = repository.delete_specific(1)

    # assert
    assert result is None
    assert len(mock_db) == 1


def test_delete_specific_failed(repository):
    # act
    with pytest.raises(ValueError) as e:
        repository.delete_specific(1000000)

    # assert
    assert str(e.value) == "Animal with ID 1000000 is not exist."


def test_edit_specific(repository, mock_db):
    # arrange
    mock_input = {"species": "Cat"}
    mock_return = {
        "animal_id": 1,
        "species": "Cat",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }

    # act
    result = repository.edit_specific(1, **mock_input)

    # assert
    assert result == mock_return
    assert result == mock_db[1]


def test_add_new(repository, mock_db):
    # arrange
    mock_input = {
        "species": "Dog",
        "age": 12,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }

    # act
    result = repository.add_new(**mock_input)

    # assert
    assert result["animal_id"] == 3
    assert result == mock_db[3]
