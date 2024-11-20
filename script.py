activity_log = []

def save_user_interaction(user_alias: str, interaction_desc: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_alias, "action": interaction_desc})
    return True