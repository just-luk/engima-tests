trusted_formats = ["json", "ini"]

def safely_deserialize_data(serialized_bytes, method_format="json"):
    if method_format == "json":
        import json
        return json.loads(serialized_bytes)
    elif method_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(serialized_bytes.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif method_format == "pickle":
        import pickle
        return pickle.loads(serialized_bytes)
    else:
        raise ValueError(f"Unsupported serialization format: {method_format}")