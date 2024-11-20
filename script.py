class Employee:
    def __init__(self, name, role, dept, wage, email):
        self.name = name
        self.role = role
        self.dept = dept
        self.wage = wage
        self.email = email

staff = [
    Employee("Alice Smith", "Software Engineer", "IT", 85000, "alice@personal.com"),
    Employee("Bob Johnson", "Project Manager", "IT", 95000, "bob@personal.com"),
    Employee("Carol Williams", "Data Analyst", "IT", 75000, "carol@personal.com")
]

def create_team_roster(team, template_str):
    roster = []
    for person in staff:
        if person.dept == team:
            roster.append(template_str.format(employee=person))
    return "\n".join(roster)