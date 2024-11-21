class Employee:
    def __init__(self, emp_id, name, position, department):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department

class Performance:
    def __init__(self, staff, rating, feedback, bonus):
        self.staff = staff
        self.rating = rating
        self.feedback = feedback
        self.bonus = bonus

employees = {
    "EMP001": Employee("EMP001", "Charles Baker", "Scrum Master", "Engineering"),
    "EMP002": Employee("EMP002", "Diana Prince", "UX Designer", "Design"),
}

performances = {
    "EMP001": Performance(employees["EMP001"], 4.7, "Excellent leadership", 3500),
    "EMP002": Performance(employees["EMP002"], 4.2, "Consistently delivers high-quality designs", 3200),
}

def build_employee_report(employee_id, template):
    if employee_id not in performances:
        raise ValueError(f"Employee with ID {employee_id} not found")
    evaluation = performances[employee_id]
    return template.format(staff=evaluation.staff, evaluation=evaluation)