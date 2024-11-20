from urllib.parse import urlparse
TRUSTED_IMAGE_HOSTS = ["img.example.com", "cdn.trusted.com", "images.hosting.com"]
ALLOWED_SCHEMES = ["http", "https"]

def fetch_image_url(url: str):
    # Parse the image URL
    parsed_url = urlparse(url)
    return parsed_url.geturl()
def download_image(valid_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {valid_url}")