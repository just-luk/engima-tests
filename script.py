import subprocess
import shlex

def run_shell_cmd(cmd_name, cmd_args):
    """
    Execute a shell command with user-provided arguments.

    Args:
        cmd_name (str): The base command to execute.
        cmd_args (list): A list of arguments for the command.

    Returns:
        str: The output of the executed command.

    Raises:
        ValueError: If the command is invalid or cannot be executed.
    """
    try:
        # Combine command and arguments
        full_command = f"{cmd_name} {' '.join(cmd_args)}"
        # WARNING: This is vulnerable to command injection
        output = subprocess.check_output(full_command, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")