class Employee:
    def __init__(self, name, job_title, team, wage, contact_info):
        self.name = name
        self.job_title = job_title
        self.team = team
        self.wage = wage
        self.contact_info = contact_info

employees = [
    Employee("Alice Smith", "Software Engineer", "IT", 85000, "alice@personal.com"),
    Employee("Bob Johnson", "Project Manager", "IT", 95000, "bob@personal.com"),
    Employee("Carol Williams", "Data Analyst", "IT", 75000, "carol@personal.com")
]

def generate_department_directory(dept_name, dir_template):
    directory = []
    for employee in employees:
        if employee.team == dept_name:
            directory.append(dir_template.format(employee=employee))
    return "\n".join(directory)