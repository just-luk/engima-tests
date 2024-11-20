from queue import Queue

task_queue = Queue()

def enqueue_task(identifier: str, details: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a task ID and associated task data and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        identifier (str): A unique identifier for the task.
        details (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": identifier, "data": details})
    return True