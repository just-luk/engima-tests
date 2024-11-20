TRUSTED_CONFIG_SIGNATURES = {
    "db_config.json": "afae23c5b1a7d5218cabc4e62357378e",
    "app_config.yaml": "9c6b74265e0e0409e4ada1aa3bdc973d"
}

# Simulated function to fetch configuration data
def fetch_config_file(filename: str):
    if filename not in TRUSTED_CONFIG_SIGNATURES:
        raise IOError(f"Configuration file {filename} does not exist")

    if filename == "db_config.json":
        return {"database": "mysql", "user": "admin", "password": "secret"}
    elif filename == "app_config.yaml":
        return {"app_name": "AwesomeApp", "version": "1.2.3"}
    else:
        return {}

def validate_config_file(filename: str, cryptographic_signature: str):
    try:
        config_data = fetch_config_file(filename)
        return config_data
    except IOError:
        return None