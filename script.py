import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def create_external_resource_link(cdn_url, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url)
    # Construct the resource URL
    res_path = f"/{res_type}/{res_id}"
    resource_link = urllib.parse.urljoin(cdn_url, res_path)
    return resource_link