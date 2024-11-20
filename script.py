ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_car_details(car: dict, changes: dict):
    car.update(changes)
    return car