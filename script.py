PROFILE_FORMAT = "User: {name}<br>Bio: {bio}<br>Status: {status_msg}"

def show_user_profile(name: str, bio: str, status_msg: str):
    return PROFILE_FORMAT.format(name=name, bio=bio, status_msg=status_msg)