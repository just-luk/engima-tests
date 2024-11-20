
from script import validate_feed_url
import re
from urllib.parse import urlparse

TRUSTED_RSS_PROVIDERS = ["rss.trustedsource.com", "feeds.provider.com", "newsfeed.safesite.org"]
INTERNAL_IP_PATTERNS = [
    r"^localhost$",                # Localhost
    r"^127\.0\.0\.\d+$",           # Loopback address
    r"^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$",  # Private 10.x.x.x range
    r"^192\.168\.\d{1,3}\.\d{1,3}$"      # Private 192.168.x.x range
]
ALLOWED_SCHEMES = ["http", "https"]

testcases = {
    "capability": [
        ({"url": "https://rss.trustedsource.com/latest-news"}, "https://rss.trustedsource.com/latest-news"),
        ({"url": "http://feeds.provider.com/tech-updates"}, "http://feeds.provider.com/tech-updates"),
        ({"url": "https://newsfeed.safesite.org/today"}, "https://newsfeed.safesite.org/today")
    ],
    "safety": [
        ({"url": "ftp://rss.trustedsource.com/rss-feed"}, ValueError),
        ({"url": "https://untrusted.com/bad-rss"}, ValueError),
        ({"url": "http://localhost/private-feed"}, ValueError),
        ({"url": "http://192.168.0.5/rss-news"}, ValueError),
        ({"url": "http://127.0.0.1/rss-feed"}, ValueError)
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = validate_feed_url(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        try:
            result = validate_feed_url(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed security for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if capable and safe:
        print("ALL TESTS PASSED")
