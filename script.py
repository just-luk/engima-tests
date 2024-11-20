approved_formats = ["json", "ini"]

def load_serialized_content(serialized_input, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(serialized_input)
    elif serialization_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(serialized_input.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(serialized_input)
    else:
        raise ValueError(f"Unsupported serialization format: {serialization_format}")