import pytest
from flask import json
from unittest.mock import MagicMock

from app import create_app
from app.employee.routes import routes

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_all_delete_route_succeed(client):
    # arrage
    routes.specific_emloyee_services.delete_specific_employee = MagicMock()
    routes.specific_emloyee_services.delete_specific_employee.return_value = None

    # act
    response = client.delete("/employees/1")

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "message": "Employee data is successfully deleted"
    }


def test_all_delete_route_failed(client):
    # arrage
    routes.specific_emloyee_services.delete_specific_employee = MagicMock()
    mock_return = "Employee with ID 1000000 is not exist."
    routes.specific_emloyee_services.delete_specific_employee.side_effect = ValueError(
        mock_return
    )

    # act
    response = client.delete("/employees/1000000")

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
