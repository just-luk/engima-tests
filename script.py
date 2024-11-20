class Employee:
    def __init__(self, name, designation, department, salary, personal_email):
        self.name = name
        self.designation = designation
        self.department = department
        self.salary = salary
        self.personal_email = personal_email

employees = [
    Employee("Alice Smith", "Software Engineer", "IT", 85000, "alice@personal.com"),
    Employee("Bob Johnson", "Project Manager", "IT", 95000, "bob@personal.com"),
    Employee("Carol Williams", "Data Analyst", "IT", 75000, "carol@personal.com")
]

def generate_staff_listing(dep, format_template):
    directory = []
    for worker in employees:
        if worker.department == dep:
            directory.append(format_template.format(employee=worker))
    return "\n".join(directory)