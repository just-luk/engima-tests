activity_log = []

def log_user_activity(user_id: str, action: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_id, "action": action})
    return True