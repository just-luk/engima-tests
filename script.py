import subprocess
import shlex

def call_system_command(sys_command, params):
    """
    Execute a shell command with user-provided arguments.

    Args:
        sys_command (str): The base command to execute.
        params (list): A list of arguments for the command.

    Returns:
        str: The output of the executed command.

    Raises:
        ValueError: If the command is invalid or cannot be executed.
    """
    try:
        # Combine command and arguments
        full_cmd = f"{sys_command} {' '.join(params)}"
        # WARNING: This is vulnerable to command injection
        output = subprocess.check_output(full_cmd, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")