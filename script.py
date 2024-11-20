from queue import Queue

task_queue = Queue()

def enqueue_task(task_identifier: str, task_details: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a task identifier and associated task details and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        task_identifier (str): A unique identifier for the task.
        task_details (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": task_identifier, "data": task_details})
    return True