allowed_methods = ["json", "csv"]

def deserialize_data(data_stream, deserialization_method="json"):
    if deserialization_method == "json":
        import json
        return json.loads(data_stream)
    elif deserialization_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(data_stream.decode()))
        return [row for row in reader]
    elif deserialization_method == "pickle":
        import pickle
        return pickle.loads(data_stream)
    else:
        raise ValueError(f"Unsupported deserialization method: {deserialization_method}")