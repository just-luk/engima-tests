activity_log = []

def record_user_action(uid: str, act_description: str) -> bool:
    global activity_log
    activity_log.append({"user_id": uid, "action": act_description})
    return True