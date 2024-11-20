PROFILE_FORMAT = "User: {fullname}<br>Bio: {biography}<br>Status: {current_status}"

def display_user_profile(fullname: str, biography: str, current_status: str):
    return PROFILE_FORMAT.format(fullname=fullname, biography=biography, current_status=current_status)