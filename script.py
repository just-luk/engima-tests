from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def assemble_redirect_uri(main_base_url, next_route):
    parsed_base = urlparse.urlparse(main_base_url)
    base_domain = parsed_base.netloc
    # Combine main_base_url with next_route to create the redirect URL
    redirect_url = urlparse.urljoin(main_base_url, next_route)
    return redirect_url