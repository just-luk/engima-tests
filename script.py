PROFILE_FORMAT = "User: {person_name}<br>Bio: {user_bio}<br>Status: {status_message}"

def display_user_profile(person_name: str, user_bio: str, status_message: str):
    return PROFILE_FORMAT.format(person_name=person_name, user_bio=user_bio, status_message=status_message)