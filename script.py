TRUSTED_DEVICE_SIGNATURES = {
    "device001": "89ebf76ae45bfcf6dd7f2aa3de8b20b3",
    "device002": "1dcfa479db7aae3d40b3984cdf202de6"
}

# Simulated function to receive a data packet from the IoT device
def receive_data_packet(iot_id: str):
    if iot_id in TRUSTED_DEVICE_SIGNATURES:
        return {"temperature": 22.5, "humidity": 60}
    else:
        raise ConnectionError(f"Failed to receive packet from device {iot_id}")

def verify_iot_signature(iot_id: str, crypto_signature: str, packet_info: dict):
    try:
        packet = receive_data_packet(iot_id)
        return packet
    except ConnectionError:
        return None