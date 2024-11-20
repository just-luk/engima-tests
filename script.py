chat_rooms = {}

def append_message_to_room(room_tag: str, sender_id: str, chat_message: str) -> bool:
    global chat_rooms
    if room_tag not in chat_rooms:
        chat_rooms[room_tag] = []
    chat_rooms[room_tag].append({"user_id": sender_id, "message": chat_message})
    return True