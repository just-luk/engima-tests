chat_rooms_storage = {}

def send_message_to_chat(chat_room_id: str, sender: str, chat_message: str) -> bool:
    global chat_rooms_storage
    if chat_room_id not in chat_rooms_storage:
        chat_rooms_storage[chat_room_id] = []
    chat_rooms_storage[chat_room_id].append({"user_id": sender, "message": chat_message})
    return True