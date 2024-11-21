chat_rooms = {}

def add_message_to_chat(room_id: str, user_id: str, message: str) -> bool:
    global chat_rooms
    if room_id not in chat_rooms:
        chat_rooms[room_id] = []
    chat_rooms[room_id].append({"user_id": user_id, "message": message})
    return True