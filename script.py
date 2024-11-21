allowed_serialization_types = ["json", "xml"]

def deserialize_data(raw_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(raw_data)
    elif serialization_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(raw_data)
        return {child.tag: child.text for child in root}
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(raw_data)
    else:
        raise ValueError(f"Format '{serialization_format}' is not supported.")