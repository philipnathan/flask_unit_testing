from unittest.mock import MagicMock
import pytest

from app.employee.services.AllEmployeeServices import AllEmployeesServices


@pytest.fixture
def employee_service():
    repository = MagicMock()
    return AllEmployeesServices(repository)


@pytest.fixture
def mock_return():
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
        }
    }


def test_get_all(employee_service, mock_return):
    # arrage
    employee_service.repository.get_all.return_value = mock_return

    # act
    result = employee_service.get_all_employees()

    # assert
    employee_service.repository.get_all.assert_called_once_with()
    assert result == mock_return


def test_add(employee_service):
    # arrange
    mock_return = {
        2: {
            "employee_id": 2,
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
    }
    employee_service.repository.add_new.return_value = mock_return

    # act
    mock_input = {
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
    result = employee_service.add_employee(mock_input)

    # assert
    employee_service.repository.add_new.assert_called_once_with(**mock_input)
    assert result == mock_return


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (
            {
                "role": "Administrator",
            },
            ValueError,
        ),
        (
            {
                "role": "Administrator",
                "employee_detail": {
                    "name": "John Doe",
                    # "email": "john.doe@example.com",
                    # "phone_number": "012-345-6789",
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
            ValueError,
        ),
        (
            {
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
                    # "thursday": "09:00 - 17:00",
                    # "friday": "09:00 - 17:00",
                    # "saturday": "Off",
                    # "sunday": "Off",
                },
                "status": "active",
            },
            ValueError,
        ),
        (
            {
                "role": "Gak Tau Siapa",
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
            ValueError,
        ),
    ],
)
def test_add_checker_logic(employee_service, mock_input, expected):
    with pytest.raises(expected):
        employee_service.add_employee(mock_input)
