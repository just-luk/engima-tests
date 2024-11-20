allowed_formats = ["json", "text"]

def process_serialfile(input_path, format_type="json"):
    with open(input_path, 'rb') as f:
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