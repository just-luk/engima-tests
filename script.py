trusted_signatures = ["json", "yaml"]

def deserialize_data(data, signature="json"):
    if signature == "json":
        import json
        return json.loads(data)
    elif signature == "yaml":
        import yaml
        return yaml.safe_load(data)
    elif signature == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported format: {format}")