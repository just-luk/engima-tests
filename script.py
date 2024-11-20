allowed_formats = ["json", "html"]

def security_content_deserializer(byte_stream, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(byte_stream)
    elif data_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(byte_stream.decode())
        return parser.result
    elif data_format == "pickle":
        import pickle
        return pickle.loads(byte_stream)
    else:
        raise ValueError(f"Unsupported format: {data_format}")