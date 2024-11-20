from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def generate_redirect_uri(auth_base_url, post_login_param):
    parsed_base = urlparse.urlparse(auth_base_url)
    base_domain = parsed_base.netloc
    # Combine auth_base_url with post_login_param to create the redirect URL
    redirect_url = urlparse.urljoin(auth_base_url, post_login_param)
    return redirect_url