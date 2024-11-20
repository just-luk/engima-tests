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

def modify_document(requester_id: str, requester_role: str, document_identifier: str, document_owner_id: str, modified_content: str):
    # Check if the document exists
    if document_identifier not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[document_identifier]["content"] = modified_content
    return DOCUMENTS_DB[document_identifier]["content"]