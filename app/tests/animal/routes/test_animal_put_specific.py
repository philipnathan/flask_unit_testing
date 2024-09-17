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


def test_specific_put_route_success(client):
    # arrange
    routes.specific_animal_services.edit_specific_animal = MagicMock()
    mock_return = {
        "animal_id": 1,
        "species": "Cat",
        "age": 3,
        "gender": "Male",
        "special_requirements": "Needs regular exercise",
    }
    routes.specific_animal_services.edit_specific_animal.return_value = mock_return

    # act
    mock_json = {
        "species": "Cat",
    }
    response = client.put(
        "/animals/1", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {
        "animal_data": mock_return,
        "message": "Animal successfully edited.",
    }


def test_specific_put_route_failed(client):
    # arrage
    routes.specific_animal_services.edit_specific_animal = MagicMock()
    mock_return = "Please check your species input"
    routes.specific_animal_services.edit_specific_animal.side_effect = ValueError(
        mock_return
    )

    # act
    mock_json = {"species": 2}
    response = client.put(
        "/animals/1", data=json.dumps(mock_json), content_type="application/json"
    )

    # assert
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {"error": mock_return}
