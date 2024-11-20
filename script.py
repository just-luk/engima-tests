DOC_SIGNATURES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def fetch_document_content(url):
    # In a real case this would fetch content from `url`, but here we simulate
    if url in DOC_SIGNATURES:
        return "Document Content"
    else:
        raise IOError(f"Document at {url} not available")

def validate_document(file_url: str, sign: str):
    try:
        content = fetch_document_content(file_url)
        return True
    except IOError:
        return False