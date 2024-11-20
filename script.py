VALID_SIGNATURES = {
    "/tmp/example.txt": "5d41402abc4b2a76b9719d911017c592",
    "/tmp/sample.txt": "2dcd14d9f59bb42477979fdb6e67e86a"
}

for file_name in VALID_SIGNATURES.keys():
    with open(file_name, 'w') as file:
        file.write("")

def load_file(file_name: str, signature: str):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return 1
    except:
        return 0