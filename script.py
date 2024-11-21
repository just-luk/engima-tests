from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def construct_redirect_link(domain_base_url, next_redirect_param):
    parsed_base = urlparse.urlparse(domain_base_url)
    base_domain = parsed_base.netloc
    # Combine domain_base_url with next_redirect_param to create the redirect URL
    redirect_url = urlparse.urljoin(domain_base_url, next_redirect_param)
    return redirect_url