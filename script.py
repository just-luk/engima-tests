import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def create_sso_url(auth_endpoint, uid, redirect_url):
    # Parse the return URL
    parsed_redirect_url = urllib.parse.urlparse(redirect_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': uid,
        'return': redirect_url
    })
    full_sso_url = f"{auth_endpoint}?{sso_params}"
    return full_sso_url