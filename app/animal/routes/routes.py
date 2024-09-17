from flask import request
from flasgger import swag_from

from .. import animal_blueprint
from ..services.AllAnimalServices import AllAnimalServices
from ..services.SpecificAnimalServices import SpecificAnimalServices
from ..repositories.AnimalRepository import AnimalRepository

all_animal_services = AllAnimalServices(AnimalRepository())
specific_animal_services = SpecificAnimalServices(AnimalRepository())


@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
@swag_from("../docs/get_specific_animal.yml")
def get_specific_animal(animal_id):
    try:
        animal = specific_animal_services.get_specific_animals(animal_id)
        return {"animal_data": animal}, 200
    except ValueError:
        return {"error": "Not Found"}, 400


@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
@swag_from("../docs/delete_specific_animal.yml")
def delete_animal(animal_id):
    try:
        specific_animal_services.delete_specific_animal(animal_id)
        return {"animal_id": animal_id, "message": "Successfully deleted."}, 200
    except ValueError as e:
        return {"error": str(e)}, 400


@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
@swag_from("../docs/update_specific_animal.yml")
def edit_animal(animal_id):
    try:
        data = request.get_json()

        result = specific_animal_services.edit_specific_animal(animal_id, data)
        return {"animal_data": result, "message": "Animal successfully edited."}, 200
    except ValueError as e:
        return {"error": str(e)}, 400


@animal_blueprint.route("/", methods=["GET"])
@swag_from("../docs/get_all_animal.yml")
def all_animal():
    return {"animal_data": all_animal_services.get_all_animal()}, 200


@animal_blueprint.route("/", methods=["POST"])
@swag_from("../docs/create_animal.yml")
def create_animal():
    try:
        data = request.get_json()

        result = all_animal_services.add_animal(data)
        return {
            "animal_data": result,
            "message": "New animal successfully created.",
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 400
