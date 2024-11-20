from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def create_forward_link(app_home_url, forward_param):
    parsed_base = urlparse.urlparse(app_home_url)
    base_domain = parsed_base.netloc
    # Combine app_home_url with forward_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_home_url, forward_param)
    return redirect_url