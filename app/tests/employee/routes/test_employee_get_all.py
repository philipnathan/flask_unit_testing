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


def test_all_get_route_succeed(client):
    # arrange
    routes.all_employees_services.get_all_employees = MagicMock()
    mock_return = {str(key): value for key, value in employees.items()}
    routes.all_employees_services.get_all_employees.return_value = mock_return

    # act
    response = client.get("/employees/")

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "employee_data": mock_return,
    }

    # mock_return: animal_id = int
    # response: animal_id = string
