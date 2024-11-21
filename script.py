ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_car_attributes(car: dict, updates: dict):
    car.update(updates)
    return car