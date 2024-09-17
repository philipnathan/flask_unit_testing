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


def test_all_put_route_succeed(client):
    # arrange
    routes.specific_emloyee_services.edit_specific_employee = MagicMock()
    mock_return = {
        "employee_id": 1,
        "role": "Administrator",
        "employee_detail": {
            "name": "Siapa hayo",
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
    routes.specific_emloyee_services.edit_specific_employee.return_value = mock_return

    # act
    mock_json = {
        "employee_detail": {
            "name": "Siapa hayo",
        }
    }
    response = client.put(
        "/employees/1", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "employee_data": mock_return,
        "message": "Employee data is successfully updated",
    }


def test_all_put_route_failed(client):
    # arrange
    routes.specific_emloyee_services.edit_specific_employee = MagicMock()
    mock_return = "Role 'test' does not exist."
    routes.specific_emloyee_services.edit_specific_employee.side_effect = ValueError(
        mock_return
    )

    # act
    mock_json = {"test": "test"}
    response = client.put(
        "/employees/1", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
