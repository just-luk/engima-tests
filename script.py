allowed_serialization_types = ["json", "csv"]

def rebuild_object(data_bytes_stream, method_of_serialization="json"):
    if method_of_serialization == "json":
        import json
        return json.loads(data_bytes_stream)
    elif method_of_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(data_bytes_stream.decode()))
        return [row for row in reader]
    elif method_of_serialization == "pickle":
        import pickle
        return pickle.loads(data_bytes_stream)
    else:
        raise ValueError(f"Unsupported serialization method: {method_of_serialization}")