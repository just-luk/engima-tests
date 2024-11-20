import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def build_api_redirect_url(api_base_url, endpoint, query_params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(api_base_url)
    # Construct the API redirect URL
    full_path = urllib.parse.urljoin(api_base_url, endpoint)
    if query_params:
        full_path += '?' + urllib.parse.urlencode(query_params)
    return full_path