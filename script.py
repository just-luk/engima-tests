PROFILE_FORMAT = "User: {username}<br>Bio: {bio}<br>Status: {status_message}"

def render_user_profile(username: str, bio: str, status_message: str):
    return PROFILE_FORMAT.format(username=username, bio=bio, status_message=status_message)