import pytest
from flask import json
from unittest.mock import MagicMock

from app import create_app
from app.employee.routes import routes
from db import employees

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_specific_get_route_succeed(client):
    # arrange
    routes.specific_emloyee_services.get_specific_employee = MagicMock()
    mock_return = {
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
    routes.specific_emloyee_services.get_specific_employee.return_value = mock_return

    # act
    response = client.get("/employees/1")

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {"employee_data": mock_return}


def test_specific_get_route_failed(client):
    # arrange
    routes.specific_emloyee_services.get_specific_employee = MagicMock()
    mock_return = "Employee with ID 1000000 is not exist."
    routes.specific_emloyee_services.get_specific_employee.side_effect = ValueError(
        mock_return
    )

    # act
    response = client.get("/employees/1000000")

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
