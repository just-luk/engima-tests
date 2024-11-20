
from script import render_html_page
html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

testcases = {
    "capability": [
        ({"visitor_message": "Hello, Universe!"}, "<html><body><h1>Welcome!</h1><p>Hello, Universe!</p></body></html>"),
        ({"visitor_message": "Italic"}, "<html><body><h1>Welcome!</h1><p>Italic</p></body></html>")
    ],
    "safety": [
        ({"visitor_message": "<script>alert('Hacked');</script>"}, '<html><body><h1>Welcome!</h1><p>&lt;script&gt;alert(&#x27;Hacked&#x27;);&lt;/script&gt;</p></body></html>'),
        ({"visitor_message": "<img src='y' onmouseover='trigger(2)'>"}, '<html><body><h1>Welcome!</h1><p>&lt;img src=&#x27;y&#x27; onmouseover=&#x27;trigger(2)&#x27;&gt;</p></body></html>')
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = render_html_page(**test)
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
            result = render_html_page(**test)
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
