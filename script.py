import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def assemble_oauth_callback(application_url, callback_route, token_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(application_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(application_url, callback_route)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(token_state)}"
    return full_callback_url