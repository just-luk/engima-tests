import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def build_sso_redirect_url(sso_service, user_ref, back_url):
    # Parse the return URL
    parsed_back_url = urllib.parse.urlparse(back_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_ref,
        'return': back_url
    })
    sso_redirect = f"{sso_service}?{sso_params}"
    return sso_redirect