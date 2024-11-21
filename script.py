chat_rooms = {}

def insert_message_in_chat(chat_id: str, sender_id: str, msg: str) -> bool:
    global chat_rooms
    if chat_id not in chat_rooms:
        chat_rooms[chat_id] = []
    chat_rooms[chat_id].append({"user_id": sender_id, "message": msg})
    return True