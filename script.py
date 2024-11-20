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

def revise_doc(usr_id: str, usr_role: str, docu_id: str, creator_id: str, updated_definition: str):
    # Check if the document exists
    if docu_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[docu_id]["content"] = updated_definition
    return DOCUMENTS_DB[docu_id]["content"]