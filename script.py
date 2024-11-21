import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def generate_oauth_token_url(app_base_url, token_path, session_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(app_base_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(app_base_url, token_path)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_state)}"
    return full_callback_url