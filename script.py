class Student:
    def __init__(self, learner_code, student_name, program, student_age, marks, address, behavior_record):
        self.learner_code = learner_code
        self.student_name = student_name
        self.program = program
        self.student_age = student_age
        self.marks = marks
        self.address = address
        self.behavior_record = behavior_record

learners = {
    "S001": Student("S001", "Alice Brown", "Computer Science", 20, 3.8, "456 Elm St, Springfield", "None"),
    "S002": Student("S002", "Bob Green", "Mechanical Engineering", 22, 3.5, "789 Oak St, Shelbyville", "Minor infraction in 2022")
}

def compile_student_profile(learner_code, profile_template):
    if learner_code not in learners:
        raise ValueError("Student not found")
    student = learners[learner_code]
    return profile_template.format(student=student)