import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

def generate_oauth_url(host_url, path_callback, session_id):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(host_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(host_url, path_callback)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_id)}"
    return full_callback_url