import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def create_api_redirect_link(base_url, path, params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    full_url = urllib.parse.urljoin(base_url, path)
    if params:
        full_url += '?' + urllib.parse.urlencode(params)
    return full_url