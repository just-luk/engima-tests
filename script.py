import os
import shlex

def execute_command_with_restrictions(cmd: str, approved_subcommands: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        cmd (str): The command string to be passed to the shell.
        approved_subcommands (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        cmd_parts = shlex.split(cmd)

        # Extract the main command and any subcommands
        main_cmd = cmd_parts[0]
        sub_cmds = cmd_parts[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if main_cmd not in approved_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(cmd).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."