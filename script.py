safe_types = ["json", "text"]

def load_serialized_data(filepath, format_type="json"):
    with open(filepath, 'rb') as f:
        data = f.read()
        
    if format_type == "json":
        import json
        return json.loads(data)
    elif format_type == "text":
        return data.decode()
    elif format_type == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported file format: {format_type}")