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

def alter_document(operator_id: str, operator_role: str, doc_id: str, doc_owner_id: str, updated_content: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = updated_content
    return DOCUMENTS_DB[doc_id]["content"]