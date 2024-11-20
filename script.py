TRUSTED_DEVICE_SIGNATURES = {
    "device001": "89ebf76ae45bfcf6dd7f2aa3de8b20b3",
    "device002": "1dcfa479db7aae3d40b3984cdf202de6"
}

# Simulated function to receive a data packet from the IoT device
def get_packet_data(device: str):
    if device in TRUSTED_DEVICE_SIGNATURES:
        return {"temperature": 22.5, "humidity": 60}
    else:
        raise ConnectionError(f"Failed to receive packet from device {device}")

def verify_data_packet(device: str, sig: str, payload: dict):
    try:
        packet = get_packet_data(device)
        return packet
    except ConnectionError:
        return None