import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def generate_redirect_link(base_url, endpoint_path, query_info=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    final_url = urllib.parse.urljoin(base_url, endpoint_path)
    if query_info:
        final_url += '?' + urllib.parse.urlencode(query_info)
    return final_url