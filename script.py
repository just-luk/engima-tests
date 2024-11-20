import re
from urllib import parse as urlparse

SCHEME_RE = re.compile(r"^[a-z]+:", re.I)

def make_location_absolute(value, host_name, url_scheme):
    # If the value already has a scheme, return it as-is
    if SCHEME_RE.search(value):
        return value
    # Normalize and make the location absolute by joining the request URI with the value
    base_url = f"{url_scheme}://{host_name}"
    new_location = urlparse.urljoin(base_url, value)

    return new_location