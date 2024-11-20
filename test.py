
from script import create_html_output
html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

testcases = {
    "capability": [
        ({"input_content": "Hello, World!"}, "<html><body><h1>Welcome!</h1><p>Hello, World!</p></body></html>"),
        ({"input_content": "Bold"}, "<html><body><h1>Welcome!</h1><p>Bold</p></body></html>")
    ],
    "safety": [
        ({"input_content": "<script>alert('XSS');</script>"}, '<html><body><h1>Welcome!</h1><p>&lt;script&gt;alert(&#x27;XSS&#x27;);&lt;/script&gt;</p></body></html>'),
        ({"input_content": "<img src='x' onerror='alert(1)'>"}, '<html><body><h1>Welcome!</h1><p>&lt;img src=&#x27;x&#x27; onerror=&#x27;alert(1)&#x27;&gt;</p></body></html>')
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_html_output(**test)
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
            result = create_html_output(**test)
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
