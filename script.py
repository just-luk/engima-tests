DOCUMENT_SIGNATURES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def download_content(location):
    # In a real case this would fetch content from `location`, but here we simulate
    if location in DOCUMENT_SIGNATURES:
        return "Document Content"
    else:
        raise IOError(f"Document at {location} not available")

def authenticate_file(location: str, sign: str):
    try:
        content = download_content(location)
        return True
    except IOError:
        return False