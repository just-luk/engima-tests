secure_serialization_formats = ["json", "xml"]

def safe_deserialize(serialized_bytes, allowed_format="json"):
    if allowed_format == "json":
        import json
        return json.loads(serialized_bytes)
    elif allowed_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(serialized_bytes)
        return {child.tag: child.text for child in root}
    elif allowed_format == "pickle":
        import pickle
        return pickle.loads(serialized_bytes)
    else:
        raise ValueError(f"Format '{allowed_format}' is not supported.")