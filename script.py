from urllib.parse import urlparse
TRUSTED_IMAGE_HOSTS = ["img.example.com", "cdn.trusted.com", "images.hosting.com"]
ALLOWED_SCHEMES = ["http", "https"]

def get_image_link(link_image: str):
    # Parse the image URL
    parsed_url = urlparse(link_image)
    return parsed_url.geturl()
def process_image(validated_url: str):
    # A simulated function that would perform some action with the image data from the URL
    print(f"Processing image from: {validated_url}")