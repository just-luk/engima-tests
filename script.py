ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_vehicle_data(vehicle_info: dict, changes_to_apply: dict):
    vehicle_info.update(changes_to_apply)
    return vehicle_info