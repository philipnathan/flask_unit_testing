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


def test_specific_get_route_succeed(client):
    # Arrange
    routes.specific_animal_services.get_specific_animals = MagicMock()
    mock_return = {
        "age": 3,
        "animal_id": 1,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
        "species": "Dog",
    }
    routes.specific_animal_services.get_specific_animals.return_value = mock_return

    # act
    response = client.get("/animals/1")

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {"animal_data": mock_return}


def test_specific_get_route_failed(client):
    # Arrange
    routes.specific_animal_services.get_specific_animals = MagicMock()
    mock_return = "Not Found"
    routes.specific_animal_services.get_specific_animals.side_effect = ValueError(
        mock_return
    )

    # act
    response = client.get("/animals/1000000")

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
