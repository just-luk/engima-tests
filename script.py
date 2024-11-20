from urllib.parse import urlparse

APPROVED_API_DOMAINS = ["api.service.com", "hooks.webapp.com"]
INTERNAL_IP_RANGES = ["localhost", "127.0.0.1", "10.", "192.168."]

def analyze_webhook(webhook_address: str):
    # Parse the webhook URL
    parsed_url = urlparse(webhook_address)
    return parsed_url.geturl()
def trigger_internal_api(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")