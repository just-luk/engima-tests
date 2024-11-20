PROFILE_FORMAT = "User: {user_name}<br>Bio: {biography}<br>Status: {status}"

def create_user_profile(user_name: str, biography: str, status: str):
    return PROFILE_FORMAT.format(user_name=user_name, biography=biography, status=status)