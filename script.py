TRUSTED_USER_PROFILES = {
    "user_abc": "4e99a098d57cbf9c6f67f176106769fb",
    "user_xyz": "12e4b2f76650484030e4d447d0b5f723"
}


# Simulated function for fetching user profile data from remote service
def get_profile_from_service(uid: str):
    if uid in TRUSTED_USER_PROFILES:
        return {"name": "Test User", "email": f"{uid}@example.com"}
    else:
        raise ConnectionError(f"Could not fetch profile for user_id {uid}")

def retrieve_user_data(uid: str, sig: str):
    try:
        profile_data = get_profile_from_service(uid)
        return profile_data
    except ConnectionError:
        return None