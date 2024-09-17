import pytest
from flask import json
from unittest.mock import MagicMock

from app import create_app
from app.animal.routes import routes

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_specific_delete_route_succeed(client):
    # arrange
    routes.specific_animal_services.delete_specific_animal = MagicMock()
    routes.specific_animal_services.delete_specific_animal.return_value = None

    # act
    response = client.delete("/animals/1")

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "animal_id": 1,
        "message": "Successfully deleted.",
    }


def test_specific_delete_route_failed(client):
    routes.specific_animal_services.delete_specific_animal = MagicMock()
    mock_return = "Animal with ID 1000000 is not exist."
    routes.specific_animal_services.delete_specific_animal.side_effect = ValueError(
        mock_return
    )

    # act
    response = client.delete("/animals/1000000")

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
