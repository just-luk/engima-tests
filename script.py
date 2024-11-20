import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def build_cdn_resource_url(cdn_url_base, file_id, file_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url_base)
    # Construct the resource URL
    file_path = f"/{file_type}/{file_id}"
    complete_url = urllib.parse.urljoin(cdn_url_base, file_path)
    return complete_url