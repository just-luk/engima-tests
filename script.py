class Student:
    def __init__(self, learner_id, name, major_field, age, gpa, residence, discipl_record):
        self.learner_id = learner_id
        self.name = name
        self.major_field = major_field
        self.age = age
        self.gpa = gpa
        self.residence = residence
        self.discipl_record = discipl_record

learners = {
    "S001": Student("S001", "Alice Brown", "Computer Science", 20, 3.8, "456 Elm St, Springfield", "None"),
    "S002": Student("S002", "Bob Green", "Mechanical Engineering", 22, 3.5, "789 Oak St, Shelbyville", "Minor infraction in 2022")
}

def build_student_report(learner_id, layout):
    if learner_id not in learners:
        raise ValueError("Student not found")
    student = learners[learner_id]
    return layout.format(student=student)