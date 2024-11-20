allowed_formats = ["json", "html"]

def deserialize_content_stream(stream, stream_format="json"):
    if stream_format == "json":
        import json
        return json.loads(stream)
    elif stream_format == "html":
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
    elif stream_format == "pickle":
        import pickle
        return pickle.loads(stream)
    else:
        raise ValueError(f"Unsupported format: {stream_format}")