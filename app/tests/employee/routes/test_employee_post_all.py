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


def test_all_post_route_succeed(client):
    # arrange
    routes.all_employees_services.add_employee = MagicMock()
    mock_return = {
        "employee_id": 4,
        "role": "Administrator",
        "employee_detail": {
            "name": "Siapa ya",
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
    routes.all_employees_services.add_employee.return_value = mock_return

    # act
    mock_json = {
        "role": "Administrator",
        "employee_detail": {
            "name": "Siapa ya",
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

    response = client.post(
        "/employees/", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "employee_data": mock_return,
        "message": "New employee is successfully added.",
    }


def test_all_post_route_failed(client):
    # arrange
    routes.all_employees_services.add_employee = MagicMock()
    mock_return = "Missing key: role"
    routes.all_employees_services.add_employee.side_effect = ValueError(mock_return)

    # act
    mock_json = {
        "employee_detail": {
            "name": "Siapa ya",
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
    response = client.post(
        "/employees/", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
