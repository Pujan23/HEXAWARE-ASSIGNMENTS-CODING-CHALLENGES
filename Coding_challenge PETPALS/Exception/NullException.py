class NullReferenceException(Exception):
    pass

def display_available_pets(shelter):
    try:
        for pet in shelter.available_pets:
            if pet.name is None or pet.age is None or pet.breed is None:
                raise NullReferenceException("Pet information is missing.")
            print(pet)
    except NullReferenceException as e:
        print(f"Null Reference: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
