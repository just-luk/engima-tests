import requests
from urllib.parse import urlparse
ALLOWED_DOMAINS = ["example.com", "trusted.com"]
ALLOWED_SCHEMES = ["http", "https"]

def parse_url(url: str):
    # Parse the URL
    parsed_url = urlparse(url)
    return parsed_url
def fetch_data(parsed_url: urlparse):
    response = requests.get(parsed_url)
    return response.text