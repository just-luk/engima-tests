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

def alter_document(modifier_id: str, user_role: str, doc_identifier: str, creator_id: str, updated_content: str):
    # Check if the document exists
    if doc_identifier not in DOCUMENTS_DB:
        raise PermissionError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_identifier]["content"] = updated_content
    return DOCUMENTS_DB[doc_identifier]["content"]