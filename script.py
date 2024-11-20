import os
import shlex

def restricted_command_executor(user_command: str, whitelist_commands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        user_command (str): The command string to be passed to the shell.
        whitelist_commands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        command_parts = shlex.split(user_command)

        # Extract the main command and any subcommands
        base_command = command_parts[0]
        additional_parts = command_parts[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if base_command not in whitelist_commands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(user_command).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."