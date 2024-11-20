from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def generate_redirect_link(app_base_url, redirect_param):
    parsed_base = urlparse.urlparse(app_base_url)
    base_domain = parsed_base.netloc
    # Combine app_base_url with redirect_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_base_url, redirect_param)
    return redirect_url