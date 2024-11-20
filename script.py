chat_rooms = {}

def log_chat_message(target_room: str, author_identifier: str, text_message: str) -> bool:
    global chat_rooms
    if target_room not in chat_rooms:
        chat_rooms[target_room] = []
    chat_rooms[target_room].append({"user_id": author_identifier, "message": text_message})
    return True