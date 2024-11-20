allowed_formats = ["json", "html"]

def deserialize_stream(serialized_data, stream_format="json"):
    if stream_format == "json":
        import json
        return json.loads(serialized_data)
    elif stream_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(serialized_data.decode())
        return parser.result
    elif stream_format == "pickle":
        import pickle
        return pickle.loads(serialized_data)
    else:
        raise ValueError(f"Unsupported format: {stream_format}")