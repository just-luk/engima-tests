import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def build_sso_redirect(auth_endpoint, uid, redirect_url):
    # Parse the return URL
    parsed_return_url = urllib.parse.urlparse(redirect_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': uid,
        'return': redirect_url
    })
    sso_redirect = f"{auth_endpoint}?{sso_params}"
    return sso_redirect