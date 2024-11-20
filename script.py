import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def build_sso_redirect_link(sso_service_url, user_identifier, redirect_back_url):
    # Parse the return URL
    parsed_return_back_url = urllib.parse.urlparse(redirect_back_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_back_url
    })
    sso_redirect = f"{sso_service_url}?{sso_params}"
    return sso_redirect