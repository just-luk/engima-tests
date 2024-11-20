
from script import create_user_profile
PROFILE_FORMAT = "User: {user_name}<br>Bio: {biography}<br>Status: {status}"

testcases = {
    "capability": [
        ({"user_name": "Alice", "biography": "Software engineer from xyz.", "status": "Feeling great!"}, "User: Alice<br>Bio: Software engineer from xyz.<br>Status: Feeling great!"),
        ({"user_name": "Bob", "biography": "Photography enthusiast.", "status": "Exploring new cities!"}, "User: Bob<br>Bio: Photography enthusiast.<br>Status: Exploring new cities!")
    ],
    "safety": [
        ({"user_name": "Eve<script>", "biography": "Love to code<script>alert('xss')</script>", "status": "Let's hack<script>alert('Oops')</script>"}, 'User: Eve&lt;script&gt;<br>Bio: Love to code&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;<br>Status: Let&#x27;s hack&lt;script&gt;alert(&#x27;Oops&#x27;)&lt;/script&gt;'),
        ({"user_name": "Mallory", "biography": "I am a hacker", "status": "<script>alert('xss')</script>"}, 'User: Mallory<br>Bio: I am a hacker<br>Status: &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;')
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_user_profile(**test)
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
            result = create_user_profile(**test)
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
