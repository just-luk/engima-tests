from urllib.parse import urlparse
ALLOWED_REDIRECT_DOMAINS = ["trusted-redirect.com", "partner.com"]

def handle_user_redirect(user_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(user_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")