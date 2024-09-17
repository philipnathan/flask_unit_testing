from db import animal_sample


class AnimalRepository:
    def __init__(self):
        self.repository = animal_sample

    def get_all(self):
        return self.repository

    def get_by_id(self, animal_id):
        if animal_id not in self.repository:
            raise ValueError(f"Animal with ID {animal_id} is not exist.")
        else:
            return self.repository[animal_id]

    def delete_specific(self, animal_id):
        # check if animal_id is exist
        if animal_id in animal_sample:
            del self.repository[animal_id]
        else:
            raise ValueError(f"Animal with ID {animal_id} is not exist.")

    def edit_specific(self, animal_id, **kwargs):
        for key, value in kwargs.items():
            self.repository[animal_id][key] = value

        result = animal_sample[animal_id]

        return result

    def add_new(self, **kwargs):
        animal_id = max(list(animal_sample.keys())) + 1
        new_animal = {}

        # add animal_id
        new_animal["animal_id"] = animal_id

        for key, value in kwargs.items():
            if key == "special_requirements":
                new_animal["special_requirements"] = value if value else ""
            else:
                new_animal[key] = value

        # add data in animal_sample, with animal_id as the key
        self.repository[animal_id] = new_animal

        return new_animal
