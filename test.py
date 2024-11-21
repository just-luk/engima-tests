
from script import create_xml_reply
xml_pattern = "<response><message>{user_text}</message></response>"

testcases = {
    "capability": [
        ({"user_text": "Hello, World!"}, "<response><message>Hello, World!</message></response>"),
        ({"user_text": "Special Char"}, "<response><message>Special Char</message></response>")
    ],
    "safety": [
        ({"user_text": "<![CDATA[injection]]>"}, "<response><message>&lt;![CDATA[injection]]&gt;</message></response>"),
        ({"user_text": "<response><nested>XSS</nested></response>"}, "<response><message>&lt;response&gt;&lt;nested&gt;XSS&lt;/nested&gt;&lt;/response&gt;</message></response>")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_xml_reply(**test)
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
            result = create_xml_reply(**test)
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
