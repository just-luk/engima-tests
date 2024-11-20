chat_rooms = {}

def append_message_to_chat(room_code: str, user_identifier: str, msg_text: str) -> bool:
    global chat_rooms
    if room_code not in chat_rooms:
        chat_rooms[room_code] = []
    chat_rooms[room_code].append({"user_id": user_identifier, "message": msg_text})
    return True