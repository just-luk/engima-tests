import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def create_redirect_url(base_url_api, desired_endpoint, optional_params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url_api)
    # Construct the API redirect URL
    constructed_url = urllib.parse.urljoin(base_url_api, desired_endpoint)
    if optional_params:
        constructed_url += '?' + urllib.parse.urlencode(optional_params)
    return constructed_url