from urllib import parse as urlparse

PERMITTED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

def construct_redirect_url(main_url, target_param):
    parsed_base = urlparse.urlparse(main_url)
    base_domain = parsed_base.netloc
    # Combine main_url with target_param to create the redirect URL
    redirect_url = urlparse.urljoin(main_url, target_param)
    return redirect_url