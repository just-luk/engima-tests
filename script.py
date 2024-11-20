ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def adjust_vehicle_info(auto: dict, modifications: dict):
    auto.update(modifications)
    return auto