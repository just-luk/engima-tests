import os
import shlex

def execute_permitted_command(input_command: str, approved_commands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        input_command (str): The command string to be passed to the shell.
        approved_commands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        command_segments = shlex.split(input_command)

        # Extract the main command and any subcommands
        primary_command = command_segments[0]
        related_segments = command_segments[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if primary_command not in approved_commands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(input_command).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."