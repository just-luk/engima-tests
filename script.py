from urllib.parse import urlparse
VALID_REDIRECT_DOMAINS = ["trusted-redirect.com", "partner.com"]

def secure_user_redirect(url_input: str):
    # Parse the user-provided URL
    parsed_link = urlparse(url_input)
    return parsed_link.geturl()
def initiate_redirect(validated_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {validated_url}")