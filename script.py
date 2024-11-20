import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def construct_external_resource_url(cdn_base_url, resource_id, resource_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_base_url)
    # Construct the resource URL
    resource_path = f"/{resource_type}/{resource_id}"
    resource_url = urllib.parse.urljoin(cdn_base_url, resource_path)
    return resource_url