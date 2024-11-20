safe_formats = ["json", "xml"]

def deserialize_data(input_data, data_type="json"):
    if data_type == "json":
        import json
        return json.loads(input_data)
    elif data_type == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(input_data)
        return {child.tag: child.text for child in root}
    elif data_type == "pickle":
        import pickle
        return pickle.loads(input_data)
    else:
        raise ValueError(f"Format '{data_type}' is not supported.")