EDITABLE_FIELDS = {"name", "position", "department"}

def edit_profile_data(profile: dict, modifications: dict, is_superuser: bool):
    if is_superuser:
        profile.update(modifications)
    else:
        for key, value in modifications.items():
            profile[key] = value
    return profile