PROFILE_FORMAT = "User: {full_name}<br>Bio: {about_me}<br>Status: {status_update}"

def generate_user_profile(full_name: str, about_me: str, status_update: str):
    return PROFILE_FORMAT.format(full_name=full_name, about_me=about_me, status_update=status_update)