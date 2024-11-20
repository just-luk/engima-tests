import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def create_cdn_resource_link(cdn_url_base, resource_identifier, type_of_resource):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url_base)
    # Construct the resource URL
    resource_path = f"/{type_of_resource}/{resource_identifier}"
    resource_url = urllib.parse.urljoin(cdn_url_base, resource_path)
    return resource_url