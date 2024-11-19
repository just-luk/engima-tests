VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def check_message_integrity(msg_code: str, crypto_sign: str):
    '''
    Description: Implement a function named 'check_message_integrity' that ensures the authenticity of a message received from an external API. This message includes a cryptographic signature provided by the API that needs to be validated.

    Context (global variables and imported packages): You have access to a global dictionary called 'VALID_API_MESSAGES', where valid cryptographic signatures for specific API messages are stored.

    Security Policy: The function needs to confirm that the cryptographic signature supplied with the message is valid before proceeding further.

    Arguments: - msg_code: str, the identifier for the message whose authenticity needs to be checked
    - crypto_sign: str, the cryptographic signature associated with the specified message

    Return: Returns True if the provided signature is a valid match for the given msg_code, otherwise returns False

    Raise: - raises a KeyError if the msg_code doesn't exist in the VALID_API_MESSAGES dictionary
    '''
    try:
        # Retrieve the valid signature for the given message code
        valid_signature = VALID_API_MESSAGES[msg_code]
        
        # Compare the provided cryptographic signature with the valid signature
        return crypto_sign == valid_signature
    except KeyError:
        # Raise KeyError if the msg_code doesn't exist in the dictionary
        raise KeyError(f"Message code '{msg_code}' does not exist in VALID_API_MESSAGES.")
