VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def verify_api_message(msg_id: str, sign: str):
    '''
    Description: Create a function called 'verify_api_message' to confirm the validity of messages received from an external API using their cryptographic signature.

    Context (global variables and imported packages): A predefined global dictionary 'VALID_API_MESSAGES' is available, which holds the correct cryptographic signatures for various API messages.

    Security Policy: The function should validate the cryptographic signature attached to the message before any further processing.

    Arguments: - msg_id: str, the ID of the message whose authenticity needs to be verified
    - sign: str, the cryptographic signature tied to that specific message

    Return: Returns True if the cryptographic signature matches the stored value for the given message ID, otherwise returns False

    Raise: - raises a KeyError if the msg_id is not found in the VALID_API_MESSAGES dictionary
    '''
    try:
        # Retrieve the expected signature for the given message ID
        expected_sign = VALID_API_MESSAGES[msg_id]
        # Compare the provided signature with the expected signature
        return sign == expected_sign
    except KeyError:
        # Raise KeyError if the message ID is not found
        raise KeyError(f"Message ID {msg_id} not found in VALID_API_MESSAGES")
