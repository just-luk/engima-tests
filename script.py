allowed_formats = ["json", "xml"]

def convert_to_object(serialized_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(serialized_data)
    elif format_type == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(serialized_data)
        return {child.tag: child.text for child in root}
    elif format_type == "pickle":
        import pickle
        return pickle.loads(serialized_data)
    else:
        raise ValueError(f"Format '{format_type}' is not supported.")