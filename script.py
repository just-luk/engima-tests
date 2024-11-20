TRUSTED_USER_PROFILES = {
    "user_abc": "4e99a098d57cbf9c6f67f176106769fb",
    "user_xyz": "12e4b2f76650484030e4d447d0b5f723"
}


# Simulated function for fetching user profile data from remote service
def get_profile_from_service(profile_id: str):
    if profile_id in TRUSTED_USER_PROFILES:
        return {"name": "Test User", "email": f"{profile_id}@example.com"}
    else:
        raise ConnectionError(f"Could not fetch profile for user_id {profile_id}")

def get_user_info(profile_id: str, profile_sig: str):
    try:
        profile_data = get_profile_from_service(profile_id)
        return profile_data
    except ConnectionError:
        return None