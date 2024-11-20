PROFILE_FORMAT = "User: {username}<br>Bio: {biography}<br>Status: {status}"

def generate_user_profile(username: str, biography: str, status: str):
    return PROFILE_FORMAT.format(username=username, biography=biography, status=status)