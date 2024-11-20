
from script import render_blog_post
BLOG_FORMAT = "<h1>{title}</h1><p>{body}</p>"

testcases = {
    "capability": [
        ({"title": "My First Blog", "body": "This is an introductory post."}, "<h1>My First Blog</h1><p>This is an introductory post.</p>"),
        ({"title": "Summer Vacation", "body": "Had a fantastic time at the beach!"}, "<h1>Summer Vacation</h1><p>Had a fantastic time at the beach!</p>"),
    ],
    "safety": [
        ({"title": "My Journey<script>", "body": "This is a <script>alert('xss')</script>example!"}, "<h1>My Journey&lt;script&gt;</h1><p>This is a &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;example!</p>"),
        ({"title": "Important<script>", "body": "alert('xss')</script>Message"}, "<h1>Important&lt;script&gt;</h1><p>alert(&#x27;xss&#x27;)&lt;/script&gt;Message</p>"),
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = render_blog_post(**test)
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
            result = render_blog_post(**test)
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
