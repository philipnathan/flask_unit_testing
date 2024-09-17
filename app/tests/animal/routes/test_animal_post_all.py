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


def test_all_post_route_succeed(client):
    # arrange
    routes.all_animal_services.add_animal = MagicMock()
    mock_return = {
        "animal_id": 4,
        "species": "Dog",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    routes.all_animal_services.add_animal.return_value = mock_return

    # act
    mock_json = {
        "species": "Dog",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    response = client.post(
        "/animals/", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "animal_data": mock_return,
        "message": "New animal successfully created.",
    }


def test_all_post_route_failed(client):
    # arrange
    routes.all_animal_services.add_animal = MagicMock()
    mock_return = "Please check your species input"
    routes.all_animal_services.add_animal.side_effect = ValueError(mock_return)

    # act
    mock_json = {
        "species": 123,
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    response = client.post(
        "/animals/", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
