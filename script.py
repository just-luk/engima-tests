from urllib.parse import urlparse
TRUSTED_IMAGE_HOSTS = ["img.example.com", "cdn.trusted.com", "images.hosting.com"]
ALLOWED_SCHEMES = ["http", "https"]

def validate_image_source(img_src: str):
    # Parse the image URL
    parsed_url = urlparse(img_src)
    return parsed_url.geturl()
def handle_image(validated_url: str):
    # A simulated function that would handle the image data from the URL
    print(f"Handling image from: {validated_url}")