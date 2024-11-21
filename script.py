from queue import Queue

task_queue = Queue()

def register_new_task(task_reference: str, parameters: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a task reference and associated task parameters and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        task_reference (str): A unique identifier for the task.
        parameters (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": task_reference, "data": parameters})
    return True