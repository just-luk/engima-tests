VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

def check_api_signature(api_message: str, sig: str):
    '''
    Description: Develop a function 'check_api_signature' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.

    Context (global variables and imported packages): You are provided with a global dictionary called 'VALID_API_MESSAGES', which stores the expected cryptographic signatures for different API messages.

    Security Policy: Ensure that the function verifies the cryptographic signature of the message before any further action is taken.

    Arguments: - api_message: str, a unique identifier for the message being checked
    - sig: str, the cryptographic signature that needs to be validated against the stored signature

    Return: The function should return True if the cryptographic signature is valid for the given api_message, else return False

    Raise: - if the given api_message does not exist in the 'VALID_API_MESSAGES' dictionary, a KeyError must be raised
    '''
    try:
        # Retrieve the expected signature for the given api_message
        expected_sig = VALID_API_MESSAGES[api_message]
        
        # Compare the provided signature with the expected signature
        if sig == expected_sig:
            return True
        else:
            return False
    except KeyError:
        # Raise KeyError if the api_message is not found in the dictionary
        raise KeyError(f"The api_message '{api_message}' does not exist in the VALID_API_MESSAGES dictionary.")
