activity_log = []

def log_user_event(user_key: str, action_details: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_key, "action": action_details})
    return True