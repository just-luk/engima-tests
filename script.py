from queue import Queue

task_queue = Queue()

def queue_new_task(unique_task_id: str, task_info: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a unique task ID and associated task information and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        unique_task_id (str): A unique identifier for the task.
        task_info (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": unique_task_id, "data": task_info})
    return True