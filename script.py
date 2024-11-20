ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_auto_data(auto_details: dict, field_updates: dict):
    auto_details.update(field_updates)
    return auto_details