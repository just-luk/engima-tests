DOCUMENTS_DB = {
    "doc123": {
        "document_id": "doc123",
        "owner_id": "user111",
        "content": "Original content of doc123"
    },
    "doc456": {
        "document_id": "doc456",
        "owner_id": "user222",
        "content": "Original content of doc456"
    }
}

def update_document(user_id: str, user_role: str, document_id: str, owner_id: str, new_content: str):
    # Check if the document exists
    if document_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[document_id]["content"] = new_content
    return DOCUMENTS_DB[document_id]["content"]