VALID_ATTRIBUTES = ["name", "email", "age"]

def update_user_attributes(user: dict, data: dict):
    user.update(data)
    return user