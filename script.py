class UserInfo:
    def __init__(self):
        self.user_name = "admin"
        self.user_password = "password123"

def format_string(string):
    userinfo = UserInfo()
    return string.format(userinfo=userinfo)