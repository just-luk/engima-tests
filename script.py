import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def construct_redirect_url(main_url, endpoint_name, params_dict=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(main_url)
    # Construct the API redirect URL
    redirect_url = urllib.parse.urljoin(main_url, endpoint_name)
    if params_dict:
        redirect_url += '?' + urllib.parse.urlencode(params_dict)
    return redirect_url