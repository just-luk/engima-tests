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
    try:
        # Split the command into a list of components safely
        components = shlex.split(input_command)

        # Extract the main command and any subcommands
        base_command = components[0]
        subcommands = components[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if base_command not in permitted_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(input_command).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."