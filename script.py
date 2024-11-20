import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def build_oauth_redirect_url(main_url, redirect_endpoint, session_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(main_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(main_url, redirect_endpoint)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_state)}"
    return full_callback_url