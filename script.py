class Student:
    def __init__(self, student_number, name, course, age, gpa, home_address, discipline_record):
        self.student_number = student_number
        self.name = name
        self.course = course
        self.age = age
        self.gpa = gpa
        self.home_address = home_address
        self.discipline_record = discipline_record

students = {
    "S003": Student("S003", "Charles Black", "Biology", 21, 3.9, "654 Pine St, Royal City", "None"),
    "S004": Student("S004", "Diane White", "Civil Engineering", 23, 3.6, "321 Maple St, Capital Town", "None"),
}

def draft_student_report(student_number, report_template):
    if student_number not in students:
        raise ValueError("Student not found")
    student = students[student_number]
    return report_template.format(student=student)