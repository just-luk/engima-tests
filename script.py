allowed_formats = ["json", "html"]

def parse_serialized_content(content, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(content)
    elif format_type == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(content.decode())
        return parser.result
    elif format_type == "pickle":
        import pickle
        return pickle.loads(content)
    else:
        raise ValueError(f"Unsupported format: {format_type}")