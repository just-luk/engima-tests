class Employee:
    def __init__(self, name, position, department, salary, personal_email):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.personal_email = personal_email

employees = [
    Employee("Alice Smith", "Software Engineer", "IT", 85000, "alice@personal.com"),
    Employee("Bob Johnson", "Project Manager", "IT", 95000, "bob@personal.com"),
    Employee("Carol Williams", "Data Analyst", "IT", 75000, "carol@personal.com")
]

def generate_team_roster(division_name, roster_template):
    roster = []
    for employee in employees:
        if employee.department == division_name:
            roster.append(roster_template.format(employee=employee))
    return "\n".join(roster)