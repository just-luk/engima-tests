ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_vehicle_data(vehicle_info: dict, modifications: dict):
    vehicle_info.update(modifications)
    return vehicle_info