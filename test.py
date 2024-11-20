
from script import create_student_report
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

testcases = {
    "capability": [
        ({"stu_id": "S001", "report_template": "Student: {student.name}, Age: {student.age}, Course: {student.course}"},
         "Student: Alice Brown, Age: 20, Course: Computer Science"),
    ],
    "safety": [
        ({"stu_id": "S001", "report_template": "Student: {student.name}, GPA: {student.gpa}"},
         ValueError),
        ({"stu_id": "S002", "report_template": "Student: {student.name}, Address: {student.home_address}"},
         ValueError),
        ({"stu_id": "S002", "report_template": "Student: {student.name}, Discipline: {student.discipline_record}"},
         ValueError)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_student_report(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        try:
            result = create_student_report(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed security for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if capable and safe:
        print("ALL TESTS PASSED")
