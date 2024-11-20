TRUSTED_DEVICE_SIGNATURES = {
    "device001": "89ebf76ae45bfcf6dd7f2aa3de8b20b3",
    "device002": "1dcfa479db7aae3d40b3984cdf202de6"
}

# Simulated function to receive a data packet from the IoT device
def receive_data_packet(device_id: str):
    if device_id in TRUSTED_DEVICE_SIGNATURES:
        return {"temperature": 22.5, "humidity": 60}
    else:
        raise ConnectionError(f"Failed to receive packet from device {device_id}")

def process_packet(device: str, packet_signature: str, data_packet: dict):
    try:
        packet = receive_data_packet(device)
        return packet
    except ConnectionError:
        return None