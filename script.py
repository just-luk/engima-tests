import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def build_cdn_resource_url(cdn_url, resource_identifier, resource_kind):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url)
    # Construct the resource URL
    resource_path = f"/{resource_kind}/{resource_identifier}"
    resource_url = urllib.parse.urljoin(cdn_url, resource_path)
    return resource_url