activity_log = []

def record_user_action(user_identifier: str, event: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_identifier, "action": event})
    return True