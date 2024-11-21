class Employee:
    def __init__(self, emp_id, name, position, department):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department

class Performance:
    def __init__(self, employee, rating, feedback, bonus):
        self.employee = employee
        self.rating = rating
        self.feedback = feedback
        self.bonus = bonus

employees = {
    "E101": Employee("E101", "John Doe", "Senior Software Engineer", "R&D"),
    "E102": Employee("E102", "Jane Smith", "Business Analyst", "Operations"),
}

performances = {
    "E101": Performance(employees["E101"], 4.3, "Exceeded expectations in multiple projects", 2000),
    "E102": Performance(employees["E102"], 3.8, "Consistently met expectations.", 1500),
}

def compile_performance_report(emp_id, report_template):
    if emp_id not in performances:
        raise ValueError(f"Employee with ID {emp_id} not found")
    performance = performances[emp_id]
    return report_template.format(employee=performance.employee, performance=performance)