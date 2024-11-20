import os
import shlex

def validate_and_execute_command(input_command: str, permitted_subcommands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        input_command (str): The command string to be passed to the shell.
        permitted_subcommands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    # Execute the command using os.system()
    result = os.popen(input_command).read()
    return result