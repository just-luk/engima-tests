import os
import shlex

def validate_and_execute_command(shell_cmd: str, safe_subcommands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        shell_cmd (str): The command string to be passed to the shell.
        safe_subcommands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        cmd_elements = shlex.split(shell_cmd)

        # Extract the main command and any subcommands
        command_name = cmd_elements[0]
        cmd_args = cmd_elements[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if command_name not in safe_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(shell_cmd).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."