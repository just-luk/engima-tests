secure_formats = ["json", "text"]

def handle_serialized_file(serialized_file_path, serialization_format="json"):
    with open(serialized_file_path, 'rb') as f:
        file_data = f.read()
        
    if serialization_format == "json":
        import json
        return json.loads(file_data)
    elif serialization_format == "text":
        return file_data.decode()
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(file_data)
    else:
        raise ValueError(f"Unsupported file format: {serialization_format}")