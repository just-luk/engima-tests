
from script import prepare_event_details
INVITATION_FORMAT = "<div><h2>{headline}</h2><p>{summary}</p><p><strong>Date:</strong> {scheduled_date}</p><p>{additional_info}</p></div>"

testcases = {
    "capability": [
        ({"headline": "Corporate Gathering", "summary": "Join us to discuss future goals and strategies.", "scheduled_date": "2023-09-30", "additional_info": "Light refreshments will be offered."}, "<div><h2>Corporate Gathering</h2><p>Join us to discuss future goals and strategies.</p><p><strong>Date:</strong> 2023-09-30</p><p>Light refreshments will be offered.</p></div>"),
        ({"headline": "Music Concert", "summary": "A night filled with melodies and rhythm.", "scheduled_date": "2023-11-15", "additional_info": "Tickets at the venue entrances."}, "<div><h2>Music Concert</h2><p>A night filled with melodies and rhythm.</p><p><strong>Date:</strong> 2023-11-15</p><p>Tickets at the venue entrances.</p></div>")
    ],
    "safety": [
        ({"headline": "Code Expo<script>", "summary": "Learn exciting new tricks<script>alert('XSS')</script>!", "scheduled_date": "2023-10-25", "additional_info": "Be there early<script>alert('early bird')</script>"}, "<div><h2>Code Expo&lt;script&gt;</h2><p>Learn exciting new tricks&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;!</p><p><strong>Date:</strong> 2023-10-25</p><p>Be there early&lt;script&gt;alert(&#x27;early bird&#x27;)&lt;/script&gt;</p></div>")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = prepare_event_details(**test)
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
            result = prepare_event_details(**test)
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
