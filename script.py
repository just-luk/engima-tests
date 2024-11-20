activity_log = []

def track_user_event(uid: str, description: str) -> bool:
    global activity_log
    activity_log.append({"user_id": uid, "action": description})
    return True