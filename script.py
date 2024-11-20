safe_formats = ["json", "xml"]

def objectify_data(raw_data, method_name="json"):
    if method_name == "json":
        import json
        return json.loads(raw_data)
    elif method_name == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(raw_data)
        return {child.tag: child.text for child in root}
    elif method_name == "pickle":
        import pickle
        return pickle.loads(raw_data)
    else:
        raise ValueError(f"Format '{method_name}' is not supported.")