import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def create_api_redirect_url(base_url_api, api_endpoint, opts=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url_api)
    # Construct the API redirect URL
    full_path = urllib.parse.urljoin(base_url_api, api_endpoint)
    if opts:
        full_path += '?' + urllib.parse.urlencode(opts)
    return full_path