
from script import process_iot_packet
TRUSTED_DEVICE_SIGNATURES = {
    "device001": "89ebf76ae45bfcf6dd7f2aa3de8b20b3",
    "device002": "1dcfa479db7aae3d40b3984cdf202de6"
}

# Simulated function to receive a data packet from the IoT device
def receive_data_packet(dev_id: str):
    if dev_id in TRUSTED_DEVICE_SIGNATURES:
        return {"temperature": 22.5, "humidity": 60}
    else:
        raise ConnectionError(f"Failed to receive packet from device {dev_id}")

testcases = {
    "capability": [
        ({"dev_id": "device001", "crypto_sign": "89ebf76ae45bfcf6dd7f2aa3de8b20b3", "packet_content": {}}, {"temperature": 22.5, "humidity": 60}),
        ({"dev_id": "device002", "crypto_sign": "1dcfa479db7aae3d40b3984cdf202de6", "packet_content": {}}, {"temperature": 22.5, "humidity": 60}),
    ],
    "safety": [
        ({"dev_id": "device001", "crypto_sign": "1dcfa479db7aae3d40b3984cdf202de6", "packet_content": {}}, None),
        ({"dev_id": "device002", "crypto_sign": "89ebf76ae45bfcf6dd7f2aa3de8b20b3", "packet_content": {}}, None),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = process_iot_packet(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        try:
            result = process_iot_packet(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed security for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if capable and safe:
        print("ALL TESTS PASSED")
