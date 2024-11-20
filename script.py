allowed_formats = ["json", "text"]

def interpret_serialized_content(src_file, content_type="json"):
    with open(src_file, 'rb') as f:
        data = f.read()
        
    if content_type == "json":
        import json
        return json.loads(data)
    elif content_type == "text":
        return data.decode()
    elif content_type == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported file format: {content_type}")