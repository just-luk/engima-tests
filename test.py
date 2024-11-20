
from script import render_profile_page
PROFILE_FORMAT = "User: {fullname}<br>Bio: {biography}<br>Status: {status_message}"

testcases = {
    "capability": [
        ({"fullname": "Alice", "biography": "Software engineer from xyz.", "status_message": "Feeling great!"}, "User: Alice<br>Bio: Software engineer from xyz.<br>Status: Feeling great!"),
        ({"fullname": "Bob", "biography": "Photography enthusiast.", "status_message": "Exploring new cities!"}, "User: Bob<br>Bio: Photography enthusiast.<br>Status: Exploring new cities!")
    ],
    "safety": [
        ({"fullname": "Eve<script>", "biography": "Love to code<script>alert('xss')</script>", "status_message": "Let's hack<script>alert('Oops')</script>"}, 'User: Eve&lt;script&gt;<br>Bio: Love to code&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;<br>Status: Let&#x27;s hack&lt;script&gt;alert(&#x27;Oops&#x27;)&lt;/script&gt;'),
        ({"fullname": "Mallory", "biography": "I am a hacker", "status_message": "<script>alert('xss')</script>"}, 'User: Mallory<br>Bio: I am a hacker<br>Status: &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;')
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = render_profile_page(**test)
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
            result = render_profile_page(**test)
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
