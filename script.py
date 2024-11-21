import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def generate_api_redirect(base_url, api_path, params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    full_path = urllib.parse.urljoin(base_url, api_path)
    if params:
        full_path += '?' + urllib.parse.urlencode(params)
    return full_path