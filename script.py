import os
import shlex

def filter_and_run_os_command(exec_command: str, whitelisted_subcommands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        exec_command (str): The command string to be passed to the shell.
        whitelisted_subcommands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        components = shlex.split(exec_command)

        # Extract the main command and any subcommands
        primary_command = components[0]
        subcommands = components[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if primary_command not in whitelisted_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(exec_command).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."