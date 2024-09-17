from ..repositories.AnimalRepository import AnimalRepository

animal_repository = AnimalRepository()


class AllAnimalServices:
    def __init__(self, repository: AnimalRepository):
        self.repository = repository

    def get_all_animal(self):
        return self.repository.get_all()

    def add_animal(self, data):
        self.add_animal_checker(data)

        return self.repository.add_new(**data)

    def add_animal_checker(self, data):
        avail_key = ["species", "gender", "age", "special_requirements"]
        species = data.get("species")
        age = data.get("age")
        gender = data.get("gender")

        for key, value in data.items():
            if key not in avail_key:
                raise ValueError("Please check your key input")

        check_data = [species, age, gender]

        for each_data in check_data:
            if each_data is None:
                raise ValueError("Please check your input")

        if not species or not isinstance(species, str):
            raise ValueError("Please check your species input")

        if not age or not isinstance(age, int) or age < 0:
            raise ValueError("Please check your age input")

        if (
            not gender
            or gender.lower() not in ("male", "female")
            or not isinstance(gender, str)
        ):
            raise ValueError("Please check your gender input")
