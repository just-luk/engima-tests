from queue import Queue

task_queue = Queue()

def insert_task_to_queue(job_id: str, job_data: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a task ID and associated task data and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        job_id (str): A unique identifier for the task.
        job_data (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": job_id, "data": job_data})
    return True