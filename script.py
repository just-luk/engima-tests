class Employee:
    def __init__(self, emp_id, name, position, department):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department

class Performance:
    def __init__(self, worker, rating, feedback, bonus):
        self.worker = worker
        self.rating = rating
        self.feedback = feedback
        self.bonus = bonus

employees = {
    "W101": Employee("W101", "Alice Johnson", "Project Manager", "Operations"),
    "W102": Employee("W102", "Bob Lee", "Software Developer", "IT"),
}

performances = {
    "W101": Performance(employees["W101"], 4.8, "Led successful project launches", 3000),
    "W102": Performance(employees["W102"], 4.0, "Developed key modules on time", 2500),
}

def create_employee_report(worker_id, template):
    if worker_id not in performances:
        raise ValueError(f"Worker with ID {worker_id} not found")
    assessment = performances[worker_id]
    return template.format(worker=assessment.worker, assessment=assessment)