activity_log = []

def track_user_event(user_name: str, event_description: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_name, "action": event_description})
    return True