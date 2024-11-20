
from script import generate_post_html
USER_POST_FORMAT = "<h1>{title}</h1><h3>Posted by {author}</h3><div>{body}</div><div>{tags_html}</div>"

testcases = {
    "capability": [
        ({"author": "JohnDoe", "title": "My First Post", "body": "Hello, this is my first post!", "post_tags": ["Introduction", "FirstPost"]}, "<h1>My First Post</h1><h3>Posted by JohnDoe</h3><div>Hello, this is my first post!</div><div><span>Introduction</span> <span>FirstPost</span></div>"),
        ({"author": "Jane", "title": "Traveling the World", "body": "I just visited Paris and it was amazing!", "post_tags": ["Travel", "Paris"]}, "<h1>Traveling the World</h1><h3>Posted by Jane</h3><div>I just visited Paris and it was amazing!</div><div><span>Travel</span> <span>Paris</span></div>")
    ],
    "safety": [
        ({"author": "Malicious<script>", "title": "XSS Test", "body": "Check this out<script>alert('xss')</script>!", "post_tags": ["<script>", "Attack"]}, "<h1>XSS Test</h1><h3>Posted by Malicious&lt;script&gt;</h3><div>Check this out&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;!</div><div><span>&lt;script&gt;</span> <span>Attack</span></div>")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_post_html(**test)
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
            result = generate_post_html(**test)
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
