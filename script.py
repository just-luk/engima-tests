activity_log = []

def save_user_event(user_identifier: str, task: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_identifier, "action": task})
    return True