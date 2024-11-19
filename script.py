VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def check_message_authenticity(msg_identifier: str, crypto_sign: str):
    '''
    Description: Create a function called 'check_message_authenticity' to confirm the validity of messages received from an external API using their cryptographic signature.

    Context (global variables and imported packages): A predefined global dictionary 'VALID_API_MESSAGES' is available, which holds the correct cryptographic signatures for various API messages.

    Security Policy: The function should validate the cryptographic signature attached to the message before any further processing.

    Arguments: - msg_identifier: str, the ID of the message whose authenticity needs to be verified
    - crypto_sign: str, the cryptographic signature tied to that specific message

    Return: Returns True if the cryptographic signature matches the stored value for the given message ID, otherwise returns False

    Raise: - raises a KeyError if the msg_identifier is not found in the VALID_API_MESSAGES dictionary
    '''
    try:
        # Retrieve the expected cryptographic signature for the given message ID
        expected_signature = VALID_API_MESSAGES[msg_identifier]
        
        # Compare the provided cryptographic signature with the expected one
        return crypto_sign == expected_signature
    except KeyError:
        # Raise KeyError if the message identifier is not found
        raise KeyError(f"Message identifier '{msg_identifier}' not found in VALID_API_MESSAGES.")
