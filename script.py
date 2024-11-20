DOC_HASHES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def fetch_resource(resource_url):
    # In a real case this would fetch content from `resource_url`, but here we simulate
    if resource_url in DOC_HASHES:
        return "Document Content"
    else:
        raise IOError(f"Document at {resource_url} not available")

def authenticate_document(resource_url: str, crypto_signature: str):
    try:
        content = fetch_resource(resource_url)
        return True
    except IOError:
        return False