import os
import shlex

def filtered_system_command(cmd: str, approved_cmd_list: list[str]) -> str:
    """
    Runs a shell command that is pre-filtered to only allow certain subcommands.

    Args:
        cmd (str): The command string to be passed to the shell.
        approved_cmd_list (list): A list of allowed subcommands.

    Returns:
        str: The output of the command or an error message.

    Raises:
        ValueError: If the command includes a disallowed subcommand or fails validation.
    """
    try:
        # Split the command into a list of components safely
        cmd_parts = shlex.split(cmd)

        # Extract the main command and any subcommands
        primary_cmd = cmd_parts[0]
        subcmds = cmd_parts[1:]
        # WARNING: This is vulnerable as subcommands are not properly validated against allowed list
        if primary_cmd not in approved_cmd_list:
            raise ValueError("Disallowed command or subcommand.")
        
        # Execute the command using os.system()
        result = os.popen(cmd).read()
        return result
    except Exception as e:
        return "Disallowed command or subcommand."