from ..repositories.AnimalRepository import AnimalRepository


class SpecificAnimalServices:
    def __init__(self, repository: AnimalRepository):
        self.repository = repository

    def get_specific_animals(self, id):
        return self.repository.get_by_id(id)

    def delete_specific_animal(self, id):
        self.repository.delete_specific(id)

    def edit_specific_animal(self, animal_id, data):
        # check if animal_id is exist
        selected_animal = self.repository.get_by_id(animal_id)

        # check input data
        if not isinstance(data, dict):
            raise ValueError("Input data must be a JSON")

        if not data:
            raise ValueError("JSON can not be empty")

        if data.get("animal_id"):
            raise ValueError("Please don't input animal ID directly in JSON")

        for key, value in data.items():
            if key not in selected_animal:
                raise ValueError("Please do not input non existing key")

            self.edit_specific_animal_check(key, value)

        result = self.repository.edit_specific(animal_id, **data)

        return result

    def edit_specific_animal_check(self, key, value):
        if key == "species" and (not value or not isinstance(value, str)):
            raise ValueError("Please check your species input")
        elif key == "age" and (not value or not isinstance(value, int) or value < 0):
            raise ValueError("Please check your age input")
        elif key == "gender" and (
            not value
            or not isinstance(value, str)
            or value.lower() not in ("male", "female")
        ):
            raise ValueError("Please check your gender input")
