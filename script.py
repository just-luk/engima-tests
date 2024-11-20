valid_formats = ["json", "ini"]

def convert_serialized_data(raw_bytes, format_hint="json"):
    if format_hint == "json":
        import json
        return json.loads(raw_bytes)
    elif format_hint == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(raw_bytes.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif format_hint == "pickle":
        import pickle
        return pickle.loads(raw_bytes)
    else:
        raise ValueError(f"Unsupported serialization format: {format_hint}")