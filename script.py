import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def create_resource_url(base_cdn_url, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(base_cdn_url)
    # Construct the resource URL
    resource_path = f"/{res_type}/{res_id}"
    resource_url = urllib.parse.urljoin(base_cdn_url, resource_path)
    return resource_url