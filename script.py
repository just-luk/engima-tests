ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def alter_vehicle_info(details: dict, modifications: dict):
    details.update(modifications)
    return details