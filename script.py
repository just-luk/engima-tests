allowed_serializations = ["json", "csv"]

def recover_obj(deserialized_bytes, method_for_serialization="json"):
    if method_for_serialization == "json":
        import json
        return json.loads(deserialized_bytes)
    elif method_for_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(deserialized_bytes.decode()))
        return [row for row in reader]
    elif method_for_serialization == "pickle":
        import pickle
        return pickle.loads(deserialized_bytes)
    else:
        raise ValueError(f"Unsupported serialization method: {method_for_serialization}")