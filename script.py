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

def modify_document(user_id: str, role: str, doc_id: str, doc_owner: str, new_data: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = new_data
    return DOCUMENTS_DB[doc_id]["content"]