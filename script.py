import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def construct_sso_redirect(auth_service_endpoint, user_identifier, redirect_uri):
    # Parse the return URL
    parsed_return_url = urllib.parse.urlparse(redirect_uri)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_uri
    })
    sso_redirect = f"{auth_service_endpoint}?{sso_params}"
    return sso_redirect