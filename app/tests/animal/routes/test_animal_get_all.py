import pytest
from flask import json
from unittest.mock import MagicMock

from app import create_app
from app.animal.routes import routes
from db import animal_sample

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_all_get_route_succeed(client):
    # arrange
    routes.all_animal_services.get_all_animal = MagicMock()
    mock_return = {str(key): value for key, value in animal_sample.items()}
    routes.all_animal_services.get_all_animal.return_value = mock_return

    # act
    response = client.get("/animals/")

    # arrange
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {"animal_data": mock_return}

    # mock_return: animal_id = int
    # response: animal_id = string
