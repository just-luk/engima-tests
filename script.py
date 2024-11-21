import os
import shlex

def run_shell_command_with_filters(command: str, allowed_subcommands_list: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        command (str): The command string to be passed to the shell.
        allowed_subcommands_list (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        components = shlex.split(command)

        # Extract the main command and any subcommands
        main_command = components[0]
        subcommands = components[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if main_command not in allowed_subcommands_list:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(command).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."