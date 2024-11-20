from urllib import parse as urlparse

SAFE_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def build_redirect_uri(primary_url, next_path):
    parsed_base = urlparse.urlparse(primary_url)
    base_domain = parsed_base.netloc
    # Combine primary_url with next_path to create the redirect URL
    redirect_uri = urlparse.urljoin(primary_url, next_path)
    return redirect_uri