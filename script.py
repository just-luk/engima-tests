import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def generate_external_resource_link(cdn_host_url, resource_tag, resource_category):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_host_url)
    # Construct the resource URL
    resource_path = f"/{resource_category}/{resource_tag}"
    resource_url = urllib.parse.urljoin(cdn_host_url, resource_path)
    return resource_url