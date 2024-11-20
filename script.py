activity_log = []

def record_user_action(uid: str, event: str) -> bool:
    global activity_log
    activity_log.append({"user_id": uid, "action": event})
    return True