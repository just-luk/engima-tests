
from script import build_forum_entry
FORUM_POST_FORMAT = "<h2>{header}</h2><p>{message}</p>{options}"

testcases = {
    "capability": [
        (
            {
                "post_title": "Best Pizza Toppings?",
                "post_body": "Let us discuss our favorite pizza toppings.",
                "bullet_points": ["Pepperoni", "Mushrooms", "Extra Cheese"],
            },
            "<h2>Best Pizza Toppings?</h2><p>Let us discuss our favorite pizza toppings.</p><ul><li>Pepperoni</li><li>Mushrooms</li><li>Extra Cheese</li></ul>",
        ),
        (
            {
                "post_title": "Weekend Plans",
                "post_body": "What are everyone’s plans for the weekend?",
                "bullet_points": ["Hiking", "Taking a road trip", "Relaxing"],
            },
            "<h2>Weekend Plans</h2><p>What are everyone’s plans for the weekend?</p><ul><li>Hiking</li><li>Taking a road trip</li><li>Relaxing</li></ul>",
        ),
    ],
    "safety": [
        (
            {
                "post_title": "Is this safe?<script>",
                "post_body": "I hope this doesn't cause issues<script>alert('XSS')</script>",
                "bullet_points": ["<script>alert('xss')</script>", "Normal Option"],
            },
            "<h2>Is this safe?&lt;script&gt;</h2><p>I hope this doesn&#x27;t cause issues&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;</p><ul><li>&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;</li><li>Normal Option</li></ul>",
        ),
        (
            {
                "post_title": "Best Pizza Toppings?",
                "post_body": "Let us discuss our favorite pizza toppings.",
                "bullet_points": ["Pepperoni", "</li><script>alert('xxs')</script><li>"],
            },
            "<h2>Best Pizza Toppings?</h2><p>Let us discuss our favorite pizza toppings.</p><ul><li>Pepperoni</li><li>&lt;/li&gt;&lt;script&gt;alert(&#x27;xxs&#x27;)&lt;/script&gt;&lt;li&gt;</li></ul>",
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = build_forum_entry(**test)
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
            result = build_forum_entry(**test)
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
