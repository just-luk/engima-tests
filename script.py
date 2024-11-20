import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

def construct_sso_redirect(sso_uri, user_identifier, redirect_link):
    # Parse the return URL
    parsed_redirect_link = urllib.parse.urlparse(redirect_link)
    # Generate the SSO redirect URL
    sso_query_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_link
    })
    constructed_sso_url = f"{sso_uri}?{sso_query_params}"
    return constructed_sso_url