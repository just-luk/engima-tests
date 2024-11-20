from urllib.parse import urlparse
TRUSTED_DOMAIN_LIST = ["trusted-redirect.com", "partner.com"]

def validate_safe_redirect(input_link: str):
    # Parse the user-provided URL
    safe_url = urlparse(input_link)
    return safe_url.geturl()
def action_redirect(allowed_link: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {allowed_link}")