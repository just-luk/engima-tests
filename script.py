import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def generate_api_redirect_uri(base_uri, api_endpoint, query=None):
    # Parse the API base URL
    parsed_uri = urllib.parse.urlparse(base_uri)
    # Construct the API redirect URL
    complete_url = urllib.parse.urljoin(base_uri, api_endpoint)
    if query:
        complete_url += '?' + urllib.parse.urlencode(query)
    return complete_url