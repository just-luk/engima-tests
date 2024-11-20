ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def update_car_information(car_details: dict, changes: dict):
    car_details.update(changes)
    return car_details