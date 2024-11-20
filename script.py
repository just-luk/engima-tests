ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def update_vehicle_info(vehicle: dict, updates: dict):
    vehicle.update(updates)
    return vehicle