from urllib.parse import urlparse

APPROVED_API_DOMAINS = ["api.service.com", "hooks.webapp.com"]
INTERNAL_IP_RANGES = ["localhost", "127.0.0.1", "10.", "192.168."]

def verify_webhook(webhook_endpoint: str):
    # Parse the webhook URL
    parsed_url = urlparse(webhook_endpoint)
    return parsed_url.geturl()
def activate_internal_api(safe_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {safe_url}")