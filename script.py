ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def update_vehicle_attributes(automobile: dict, changes: dict):
    automobile.update(changes)
    return automobile