from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def create_redirect_url(base_url, next_param):
    parsed_base = urlparse.urlparse(base_url)
    base_domain = parsed_base.netloc
    # Combine base_url with next_param to create the redirect URL
    redirect_url = urlparse.urljoin(base_url, next_param)
    return redirect_url