from urllib.parse import urlparse
SAFE_REDIRECT_DOMAINS = ["trusted-redirect.com", "partner.com"]

def redirect_user_safely(target_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(target_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")