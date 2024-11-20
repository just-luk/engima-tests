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

def revise_document(owner: str, editor_role: str, doc_ref: str, doc_creator: str, revised_content: str):
    # Check if the document exists
    if doc_ref not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_ref]["content"] = revised_content
    return DOCUMENTS_DB[doc_ref]["content"]