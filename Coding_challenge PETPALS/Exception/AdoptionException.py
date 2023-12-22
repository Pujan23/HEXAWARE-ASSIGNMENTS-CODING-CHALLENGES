class AdoptionException(Exception):
    pass

def adopt_pet(shelter, pet):
    try:
        if pet not in shelter.available_pets:
            raise AdoptionException("Pet is not available for adoption.")
        # Add adoption logic here
        else:
            shelter.remove_pet(pet)
            print(f"Adoption successful: {pet}")
    except AdoptionException as e:
        print(f"Adoption Exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
