import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def create_oauth_callback_url(base_url, callback_path, state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(base_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(base_url, callback_path)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(state)}"
    return full_callback_url