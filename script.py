import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

def generate_cdn_content_url(cdn_origin_url, content_id, content_kind):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_origin_url)
    # Construct the resource URL
    content_path = f"/{content_kind}/{content_id}"
    complete_url = urllib.parse.urljoin(cdn_origin_url, content_path)
    return complete_url