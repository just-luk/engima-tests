from urllib.parse import urlparse

APPROVED_API_DOMAINS = ["api.service.com", "hooks.webapp.com"]
INTERNAL_IP_RANGES = ["localhost", "127.0.0.1", "10.", "192.168."]

def validate_callback(callback_url: str):
    # Parse the webhook URL
    parsed_url = urlparse(callback_url)
    return parsed_url.geturl()
def invoke_internal_system(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")