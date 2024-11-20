from urllib.parse import urlparse
ALLOWED_REDIRECT_DOMAINS = ["trusted-redirect.com", "partner.com"]

def user_defined_redirect(redirect_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(redirect_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")