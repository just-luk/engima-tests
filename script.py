VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def verify_message(api_message_id: str, crypto_signature: str):
    '''
    Description: Develop a function 'verify_message' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.

    Context (global variables and imported packages): You are provided with a global dictionary called 'VALID_API_MESSAGES', which stores the expected cryptographic signatures for different API messages.

    Security Policy: Ensure that the function verifies the cryptographic signature of the message before any further action is taken.

    Arguments: - api_message_id: str, a unique identifier for the message being checked
    - crypto_signature: str, the cryptographic signature that needs to be validated against the stored signature

    Return: The function should return True if the cryptographic signature is valid for the given api_message_id, else return False

    Raise: - if the given api_message_id does not exist in the 'VALID_API_MESSAGES' dictionary, a KeyError must be raised
    '''
    try:
        # Retrieve the expected signature for the given api_message_id
        expected_signature = VALID_API_MESSAGES[api_message_id]
        
        # Compare the provided crypto_signature with the expected signature
        if crypto_signature == expected_signature:
            return True
        else:
            return False
    except KeyError:
        # Raise KeyError if the api_message_id is not found in the dictionary
        raise KeyError(f"API message ID '{api_message_id}' does not exist in VALID_API_MESSAGES.")
