import os
import shlex

def filter_and_run_command(cmd_input: str, permitted_subcommands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        cmd_input (str): The command string to be passed to the shell.
        permitted_subcommands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        command_parts = shlex.split(cmd_input)

        # Extract the main command and any subcommands
        primary_command = command_parts[0]
        command_subs = command_parts[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if primary_command not in permitted_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(cmd_input).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."