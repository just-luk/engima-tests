TRUSTED_CONFIG_SIGNATURES = {
    "db_config.json": "afae23c5b1a7d5218cabc4e62357378e",
    "app_config.yaml": "9c6b74265e0e0409e4ada1aa3bdc973d"
}

# Simulated function to fetch configuration data
def fetch_config_data(file_name: str):
    if file_name not in TRUSTED_CONFIG_SIGNATURES:
        raise IOError(f"Configuration file {file_name} does not exist")

    if file_name == "db_config.json":
        return {"database": "mysql", "user": "admin", "password": "secret"}
    elif file_name == "app_config.yaml":
        return {"app_name": "AwesomeApp", "version": "1.2.3"}
    else:
        return {}

def handle_config_data(file_name: str, file_signature: str):
    try:
        config_data = fetch_config_data(file_name)
        return config_data
    except IOError:
        return None