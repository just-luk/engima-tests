safe_formats = ["json", "text"]

def deserialize_file_data(input_filepath, input_format="json"):
    with open(input_filepath, 'rb') as f:
        file_content = f.read()
        
    if input_format == "json":
        import json
        return json.loads(file_content)
    elif input_format == "text":
        return file_content.decode()
    elif input_format == "pickle":
        import pickle
        return pickle.loads(file_content)
    else:
        raise ValueError(f"Unsupported file format: {input_format}")