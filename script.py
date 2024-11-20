class Student:
    def __init__(self, stu_id, name, course, age, gpa, home_address, discipline_record):
        self.stu_id = stu_id
        self.name = name
        self.course = course
        self.age = age
        self.gpa = gpa
        self.home_address = home_address
        self.discipline_record = discipline_record

students = {
    "S001": Student("S001", "Alice Brown", "Computer Science", 20, 3.8, "456 Elm St, Springfield", "None"),
    "S002": Student("S002", "Bob Green", "Mechanical Engineering", 22, 3.5, "789 Oak St, Shelbyville", "Minor infraction in 2022")
}

def create_student_report(stu_id, report_template):
    if stu_id not in students:
        raise ValueError("Student not found")
    student = students[stu_id]
    return report_template.format(student=student)