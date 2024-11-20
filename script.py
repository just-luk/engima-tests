chat_rooms = {}

def push_text_to_room(room_name: str, member_id: str, content: str) -> bool:
    global chat_rooms
    if room_name not in chat_rooms:
        chat_rooms[room_name] = []
    chat_rooms[room_name].append({"user_id": member_id, "message": content})
    return True