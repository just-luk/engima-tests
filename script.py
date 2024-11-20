secure_formats = ["json", "ini"]

def deserialize_binary_data(bin_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(bin_data)
    elif format_type == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(bin_data.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif format_type == "pickle":
        import pickle
        return pickle.loads(bin_data)
    else:
        raise ValueError(f"Unsupported serialization format: {format_type}")