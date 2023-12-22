from Entity.pet import pet


class InvalidAgeException(Exception):
    pass

def add_pet_to_shelter(shelter, name, age, breed):
    try:
        if age <= 0:
            raise InvalidAgeException("Age should be a positive integer.")
        pet = Pet(name, age, breed)
        shelter.add_pet(pet)
    except InvalidAgeException as e:
        print(f"Invalid Age: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
