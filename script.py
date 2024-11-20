secure_serialization_formats = ["json", "html"]

def deserialize_stream_data(stream, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(stream)
    elif serialization_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(stream.decode())
        return parser.result
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(stream)
    else:
        raise ValueError(f"Unsupported format: {serialization_format}")