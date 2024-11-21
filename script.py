DOCUMENT_SIGNATURES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def retrieve_content(document_location):
    # In a real case this would fetch content from `document_location`, but here we simulate
    if document_location in DOCUMENT_SIGNATURES:
        return "Document Content"
    else:
        raise IOError(f"Document at {document_location} not available")

def check_file(document_location: str, crypto_sign: str):
    try:
        content = retrieve_content(document_location)
        return True
    except IOError:
        return False