from unittest.mock import patch
import pytest

from app.employee.repositories.EmployeesRepository import EmployeesRepository


@pytest.fixture
def mock_db():
    return {
        1: {
            "employee_id": 1,
            "role": "Administrator",
            "employee_detail": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone_number": "012-345-6789",
            },
            "schedule": {
                "monday": "09:00 - 17:00",
                "tuesday": "09:00 - 17:00",
                "wednesday": "09:00 - 17:00",
                "thursday": "09:00 - 17:00",
                "friday": "09:00 - 17:00",
                "saturday": "Off",
                "sunday": "Off",
            },
            "status": "active",
        },
    }


@pytest.fixture
def mock_input():
    return {
        "role": "Administrator",
        "employee_detail": {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone_number": "012-345-6789",
        },
        "schedule": {
            "monday": "09:00 - 17:00",
            "tuesday": "09:00 - 17:00",
            "wednesday": "09:00 - 17:00",
            "thursday": "09:00 - 17:00",
            "friday": "09:00 - 17:00",
            "saturday": "Off",
            "sunday": "Off",
        },
        "status": "active",
    }


@pytest.fixture
def repository(mock_db):
    with patch("app.employee.repositories.EmployeesRepository.employees", mock_db):
        yield EmployeesRepository()


def test_get_all(repository, mock_db):
    # act
    result = repository.get_all()

    # assert
    assert result == mock_db


def test_add_new(repository, mock_input):
    # act
    result = repository.add_new(**mock_input)

    # assert
    assert result is not None
    assert result["2"] == mock_input


def test_get_specific_succeed(repository, mock_db):
    # act
    result = repository.get_specific(1)

    # assert
    assert result == mock_db[1]


def test_get_specific_failed(repository):
    # act
    with pytest.raises(ValueError) as e:
        repository.get_specific(1000000)

    # assert
    assert str(e.value) == "Employee with ID 1000000 is not exist."


def test_delete_specific_succeed(repository):
    # act
    result = repository.delete_specific(1)

    # assert
    assert result is None


def test_delete_specific_failed(repository):
    # act
    with pytest.raises(ValueError) as e:
        repository.delete_specific(1000000)

    # assert
    assert str(e.value) == "Employee with ID 1000000 is not exist."


def test_edit_specific_succeed(repository):
    # arrange
    mock_input = {"schedule": {"monday": "08:00 - 17:00"}, "status": "nonactive"}
    mock_return = {
        "employee_id": 1,
        "role": "Administrator",
        "employee_detail": {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone_number": "012-345-6789",
        },
        "schedule": {
            "monday": "08:00 - 17:00",
            "tuesday": "09:00 - 17:00",
            "wednesday": "09:00 - 17:00",
            "thursday": "09:00 - 17:00",
            "friday": "09:00 - 17:00",
            "saturday": "Off",
            "sunday": "Off",
        },
        "status": "nonactive",
    }

    # act
    result = repository.edit_specific(1, **mock_input)

    # assert
    assert result == mock_return
