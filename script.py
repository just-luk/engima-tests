DOCUMENT_SIGNATURES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def retrieve_doc_content(link):
    # In a real case this would fetch content from `link`, but here we simulate
    if link in DOCUMENT_SIGNATURES:
        return "Document Content"
    else:
        raise IOError(f"Document at {link} not available")

def check_document(doc_link: str, check_signature: str):
    try:
        content = retrieve_doc_content(doc_link)
        return True
    except IOError:
        return False