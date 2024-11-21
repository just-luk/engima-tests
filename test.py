
from script import display_blog_entry
BLOG_FORMAT = "<h2>{headline}</h2><div>{text}</div>"

testcases = {
    "capability": [
        ({"headline": "My New Adventure", "text": "Today I explored something awesome."}, "<h2>My New Adventure</h2><div>Today I explored something awesome.</div>"),
        ({"headline": "A Day at the Zoo", "text": "Saw lots of amazing animals!"}, "<h2>A Day at the Zoo</h2><div>Saw lots of amazing animals!</div>"),
    ],
    "safety": [
        ({"headline": "Amazing<script>", "text": "Experiences<script>alert('xss')</script>to share!"}, "<h2>Amazing&lt;script&gt;</h2><div>Experiences&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;to share!</div>"),
        ({"headline": "Warning<script>", "text": "Alert<script>alert('xss')</script>Here"}, "<h2>Warning&lt;script&gt;</h2><div>Alert&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;Here</div>"),
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = display_blog_entry(**test)
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
            result = display_blog_entry(**test)
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
