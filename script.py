PROFILE_FORMAT = "User: {fullname}<br>Bio: {biography}<br>Status: {status_message}"

def render_profile_page(fullname: str, biography: str, status_message: str):
    return PROFILE_FORMAT.format(fullname=fullname, biography=biography, status_message=status_message)