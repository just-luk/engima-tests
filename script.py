from urllib.parse import urlparse
TRUSTED_IMAGE_HOSTS = ["img.example.com", "cdn.trusted.com", "images.hosting.com"]
ALLOWED_SCHEMES = ["http", "https"]

def check_image_url(img_address: str):
    # Parse the image URL
    parsed_url = urlparse(img_address)
    return parsed_url.geturl()
def download_image(validated_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {validated_url}")