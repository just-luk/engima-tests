from urllib.parse import urlparse

APPROVED_API_DOMAINS = ["api.service.com", "hooks.webapp.com"]
INTERNAL_IP_RANGES = ["localhost", "127.0.0.1", "10.", "192.168."]

def handle_webhook(webhook_link: str):
    # Parse the webhook URL
    parsed_url = urlparse(webhook_link)
    return parsed_url.geturl()
def trigger_internal_api(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")