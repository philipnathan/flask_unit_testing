from unittest.mock import MagicMock
import pytest

from app.employee.services.SpecificEmployeeServices import SpecificEmployeeServices


@pytest.fixture
def employee_service():
    repository = MagicMock()
    return SpecificEmployeeServices(repository)


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


def test_get_specific(employee_service, mock_return):
    # arrange
    employee_service.repository.get_specific.return_value = mock_return

    # act
    result = employee_service.get_specific_employee(1)

    # asssert
    employee_service.repository.get_specific.assert_called_once_with(1)
    assert result == mock_return


def test_delete_specific(employee_service):
    # arrange
    employee_service.repository.delete_specific.return_value = None

    # act
    result = employee_service.delete_specific_employee(1)

    # assert
    employee_service.repository.delete_specific.assert_called_with(1)
    assert result is None


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ([], ValueError),
        ({}, ValueError),
        (
            {
                "employee_id": 1,
            },
            ValueError,
        ),
        (
            {
                "employee_detail": {
                    "name": "John Doe",
                    "email": "john.doe@example.com",
                    "phone": "012-345-6789",
                },
            },
            ValueError,
        ),
        (
            {
                "schedule": {
                    "senin": "09:00 - 17:00",
                    "selasa": "09:00 - 17:00",
                    "rabu": "09:00 - 17:00",
                },
            },
            ValueError,
        ),
        (
            {"test": "test"},
            ValueError,
        ),
    ],
)
def test_edit_specific(employee_service, mock_input, expected):
    with pytest.raises(expected):
        employee_service.edit_specific_employee(1, mock_input)
