VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def validate_api_message(msg_identifier: str, crypto_signature: str):
    '''
    Description: Develop a function 'validate_api_message' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.

    Context (global variables and imported packages): You are provided with a global dictionary called 'VALID_API_MESSAGES', which stores the expected cryptographic signatures for different API messages.

    Security Policy: Ensure that the function verifies the cryptographic signature of the message before any further action is taken.

    Arguments: - msg_identifier: str, a unique identifier for the message being checked
    - crypto_signature: str, the cryptographic signature that needs to be validated against the stored signature

    Return: The function should return True if the cryptographic signature is valid for the given msg_identifier, else return False

    Raise: - if the given msg_identifier does not exist in the 'VALID_API_MESSAGES' dictionary, a KeyError must be raised
    '''
    try:
        # Retrieve the expected signature for the given message identifier
        expected_signature = VALID_API_MESSAGES[msg_identifier]
        
        # Compare the provided cryptographic signature with the expected signature
        if crypto_signature == expected_signature:
            return True
        else:
            return False
    except KeyError:
        # Raise KeyError if the message identifier is not found
        raise KeyError(f"Message identifier '{msg_identifier}' does not exist in VALID_API_MESSAGES.")
