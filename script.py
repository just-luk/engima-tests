import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def assemble_oauth_callback_url(root_url, path_for_callback, session_token):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(root_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(root_url, path_for_callback)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_token)}"
    return full_callback_url