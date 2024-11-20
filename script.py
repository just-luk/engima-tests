activity_log = []

def track_user_operation(account: str, operation: str) -> bool:
    global activity_log
    activity_log.append({"user_id": account, "action": operation})
    return True