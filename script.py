import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def assemble_api_redirect_link(base_api_url, api_path, query_dict=None):
    # Parse the API base URL
    parsed_base_url = urllib.parse.urlparse(base_api_url)
    # Construct the API redirect URL
    full_api_url = urllib.parse.urljoin(base_api_url, api_path)
    if query_dict:
        full_api_url += '?' + urllib.parse.urlencode(query_dict)
    return full_api_url