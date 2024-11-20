supported_formats = ["json", "csv"]

def decode_data(encoded_bytes, format_name="json"):
    if format_name == "json":
        import json
        return json.loads(encoded_bytes)
    elif format_name == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(encoded_bytes.decode()))
        return [row for row in reader]
    elif format_name == "pickle":
        import pickle
        return pickle.loads(encoded_bytes)
    else:
        raise ValueError(f"Unsupported serialization method: {format_name}")