chat_rooms = {}

def post_msg_in_chat(chat_room: str, user: str, new_message: str) -> bool:
    global chat_rooms
    if chat_room not in chat_rooms:
        chat_rooms[chat_room] = []
    chat_rooms[chat_room].append({"user_id": user, "message": new_message})
    return True