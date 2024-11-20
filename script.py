import re
from urllib.parse import urlparse

ALLOWED_API_DOMAINS = ["api.trustedsource.com", "gateway.partnerapi.com"]
INTERNAL_IP_PATTERNS = [
    r"^localhost$",                # Localhost
    r"^127\.0\.0\.\d+$",           # Loopback address
    r"^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$",  # Private 10.x.x.x range
    r"^192\.168\.\d{1,3}\.\d{1,3}$"      # Private 192.168.x.x range
]

def verify_api_address(endpoint_address: str):
    # Parse the provided API URL
    parsed_url = urlparse(endpoint_address)
    return parsed_url.geturl()
def fetch_api_details(validated_address: str):
    # This is a simulated external API request
    print(f"Calling API at: {validated_address}")