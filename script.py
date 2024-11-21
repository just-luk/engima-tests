import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def generate_external_resource_url(cdn_base, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_base)
    # Construct the resource URL
    resource_path = f"/{res_type}/{res_id}"
    resource_url = urllib.parse.urljoin(cdn_base, resource_path)
    return resource_url