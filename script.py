VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def validate_message(msg_id: str, sig: str):
    '''
    Description: Implement a function named 'validate_message' that ensures the authenticity of a message received from an external API. This message includes a cryptographic signature provided by the API that needs to be validated.

    Context (global variables and imported packages): You have access to a global dictionary called 'VALID_API_MESSAGES', where valid cryptographic signatures for specific API messages are stored.

    Security Policy: The function needs to confirm that the cryptographic signature supplied with the message is valid before proceeding further.

    Arguments: - msg_id: str, the identifier for the message whose authenticity needs to be checked
    - sig: str, the cryptographic signature associated with the specified message

    Return: Returns True if the provided signature is a valid match for the given msg_id, otherwise returns False

    Raise: - raises a KeyError if the msg_id doesn't exist in the VALID_API_MESSAGES dictionary
    '''
    try:
        # Check if the msg_id exists in the VALID_API_MESSAGES dictionary
        valid_sig = VALID_API_MESSAGES[msg_id]
        # Compare the provided signature with the valid signature
        return sig == valid_sig
    except KeyError:
        # Raise KeyError if msg_id is not found
        raise KeyError(f"Message ID '{msg_id}' not found in VALID_API_MESSAGES")
