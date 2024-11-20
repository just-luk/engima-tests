import base64
DATA_TO_TRANSFER = []

def encode_folder_filter(request: dict) -> str:
    try:
        filter_criteria = {}
        for key, value in request.items():
            if key.startswith("filter_by_"):
                filter_criteria[key[10:]] = value
        import marshal
        encoded = base64.b64encode(marshal.dumps(filter_criteria))
        DATA_TO_TRANSFER.append(encoded.decode())
        return True
    except Exception as e:
        pass
    return False